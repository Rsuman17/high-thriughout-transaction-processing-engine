from db import get_connection
import uuid


def transfer_money(sender, receiver, amount):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # Start Transaction
        conn.autocommit = False

        # Lock Sender Row
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
            return {
                "status": 404,
                "error": "Sender not found"
            }

        sender_balance = float(sender_data[0])

        # Lock Receiver Row
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
            return {
                "status": 404,
                "error": "Receiver not found"
            }

        # Balance Check
        if sender_balance < amount:
            conn.rollback()
            return {
                "status": 400,
                "error": "Insufficient Balance"
            }

        # Debit Sender
        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance - %s
            WHERE name=%s
            """,
            (amount, sender)
        )

        # Credit Receiver
        cursor.execute(
            """
            UPDATE accounts
            SET balance = balance + %s
            WHERE name=%s
            """,
            (amount, receiver)
        )

        transaction_id = str(uuid.uuid4())

        # Save Transaction
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
            VALUES(%s,%s,%s,%s,%s)
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

        return {
            "status": 200,
            "message": "Transfer Successful",
            "transaction_id": transaction_id
        }

    except Exception as e:

        conn.rollback()

        return {
            "status": 500,
            "error": str(e)
        }

    finally:

        cursor.close()
        conn.close()