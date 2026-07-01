from flask import Blueprint, request, jsonify

from services.payment_service import (
    create_payment,
    get_payment,
    get_all_payments
)

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/payment", methods=["POST"])
def payment():

    data = request.get_json()

    sender = data["sender"]
    receiver = data["receiver"]
    amount = data["amount"]
    idempotency_key = data["idempotency_key"]

    result = create_payment(
        sender,
        receiver,
        amount,
        idempotency_key
    )

    return jsonify(result)

@payment_bp.route("/payment/<transaction_id>", methods=["GET"])
def payment_status(transaction_id):

    payment = get_payment(transaction_id)

    if payment is None:

        return jsonify({
            "message": "Payment not found"
        }), 404

    return jsonify({

        "id": payment[0],
        "transaction_id": str(payment[1]),
        "sender": payment[2],
        "receiver": payment[3],
        "amount": float(payment[4]),
        "status": payment[5],
        "created_at": str(payment[6])

    })


@payment_bp.route("/payments", methods=["GET"])
def all_payments():

    payments = get_all_payments()

    result = []

    for payment in payments:

        result.append({

            "transaction_id": str(payment[1]),
            "sender": payment[2],
            "receiver": payment[3],
            "amount": float(payment[4]),
            "status": payment[5]

        })

    return jsonify(result)