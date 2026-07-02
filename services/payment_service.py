import uuid
import json

from db import get_connection
from cache.redis_client import redis_client


def create_payment(sender, receiver, amount, idempotency_key):

    conn = get_connection()
    cursor = conn.cursor()

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


def get_all_transactions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM payments
        ORDER BY created_at DESC
        """
    )

    transactions = cursor.fetchall()

    cursor.close()
    conn.close()

    return transactions


def get_transaction(transaction_id):

    cache_key = f"transaction:{transaction_id}"

    cached = redis_client.get(cache_key)

    if cached:
        print("Fetched from Redis")
        return json.loads(cached)

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

    if payment:

        data = {
            "transaction_id": str(payment[1]),
            "sender": payment[2],
            "receiver": payment[3],
            "amount": float(payment[4]),
            "status": payment[5],
            "created_at": str(payment[6])
        }

        redis_client.setex(
            cache_key,
            300,
            json.dumps(data)
        )

        print("Fetched from PostgreSQL")

        return data

    return None