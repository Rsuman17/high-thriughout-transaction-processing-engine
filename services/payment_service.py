import uuid
from db import get_connection


def create_payment(sender, receiver, amount, idempotency_key):

    conn = get_connection()
    cursor = conn.cursor()

    # Check if request already processed
    cursor.execute(
        """
        SELECT transaction_id
        FROM payments
        WHERE idempotency_key=%s
        """,
        (idempotency_key,)
    )

    existing = cursor.fetchone()

    if existing:
        cursor.close()
        conn.close()

        return {
            "message": "Payment already processed",
            "transaction_id": str(existing[0])
        }

    transaction_id = str(uuid.uuid4())

    cursor.execute(
        """
        INSERT INTO payments
        (
            transaction_id,
            sender,
            receiver,
            amount,
            status,
            idempotency_key
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            transaction_id,
            sender,
            receiver,
            amount,
            "SUCCESS",
            idempotency_key
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Payment Successful",
        "transaction_id": transaction_id
    }


def get_payment(transaction_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM payments
        WHERE transaction_id=%s
        """,
        (transaction_id,)
    )

    payment = cursor.fetchone()

    cursor.close()
    conn.close()

    return payment


def get_all_payments():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM payments
        ORDER BY created_at DESC
        """
    )

    payments = cursor.fetchall()

    cursor.close()
    conn.close()

    return payments


def get_transaction(transaction_id):

    return get_payment(transaction_id)


def get_all_transactions():

    return get_all_payments()