from db import get_connection
from messaging.producer import publish_payment_event
from logging_config import logger

import uuid
import time


def transfer_money(sender, receiver, amount):

    start_time = time.time()

    conn = get_connection()
    cursor = conn.cursor()

    try:

        conn.autocommit = False

        logger.info(
            f"Transfer Started | Sender={sender} Receiver={receiver} Amount={amount}"
        )

        # ----------------------------
        # Lock Sender
        # ----------------------------
        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE name=%s
            FOR UPDATE
            """,
            (sender,)
        )

        sender_data = cursor.fetchone()

        if sender_data is None:
            conn.rollback()

            logger.warning(f"Sender not found : {sender}")

            return {
                "status": 404,
                "error": "Sender not found"
            }

        sender_balance = float(sender_data[0])

        # ----------------------------
        # Lock Receiver
        # ----------------------------
        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE name=%s
            FOR UPDATE
            """,
            (receiver,)
        )

        receiver_data = cursor.fetchone()

        if receiver_data is None:
            conn.rollback()

            logger.warning(f"Receiver not found : {receiver}")

            return {
                "status": 404,
                "error": "Receiver not found"
            }

        # ----------------------------
        # Balance Validation
        # ----------------------------
        if sender_balance < amount:
            conn.rollback()

            logger.warning(
                f"Insufficient Balance | {sender} Balance={sender_balance}"
            )

            return {
                "status": 400,
                "error": "Insufficient Balance"
            }

        # ----------------------------
        # Debit Sender
        # ----------------------------
        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance - %s
            WHERE name=%s
            """,
            (amount, sender)
        )

        # ----------------------------
        # Credit Receiver
        # ----------------------------
        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance + %s
            WHERE name=%s
            """,
            (amount, receiver)
        )

        transaction_id = str(uuid.uuid4())

        # ----------------------------
        # Save Transaction
        # ----------------------------
        cursor.execute(
            """
            INSERT INTO payments
            (
                transaction_id,
                sender,
                receiver,
                amount,
                status
            )
            VALUES (%s,%s,%s,%s,%s)
            """,
            (
                transaction_id,
                sender,
                receiver,
                amount,
                "SUCCESS"
            )
        )

        conn.commit()

        # ----------------------------
        # Kafka Event
        # ----------------------------
        event = {
            "transaction_id": transaction_id,
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "status": "SUCCESS"
        }

        publish_payment_event(event)

        execution_time = round((time.time() - start_time) * 1000, 2)

        logger.info(
            f"Transfer Successful | Transaction={transaction_id} | {execution_time} ms"
        )

        return {
            "status": 200,
            "message": "Transfer Successful",
            "transaction_id": transaction_id,
            "execution_time_ms": execution_time
        }

    except Exception as e:

        conn.rollback()

        logger.exception("Transfer Failed")

        return {
            "status": 500,
            "error": str(e)
        }

    finally:

        cursor.close()
        conn.close()