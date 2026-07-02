from flask import Blueprint, request, jsonify
from services.transfer_service import transfer_money
from services.payment_service import (
    get_all_transactions,
    get_transaction
)

transfer_bp = Blueprint("transfer", __name__)


@transfer_bp.route("/transfer", methods=["POST"])
def transfer():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    sender = data.get("sender")
    receiver = data.get("receiver")
    amount = data.get("amount")

    # Input Validation

    if not sender:
        return jsonify({
            "error": "Sender is required"
        }), 400

    if not receiver:
        return jsonify({
            "error": "Receiver is required"
        }), 400

    if sender == receiver:
        return jsonify({
            "error": "Sender and Receiver cannot be the same"
        }), 400

    if amount is None:
        return jsonify({
            "error": "Amount is required"
        }), 400

    try:
        amount = float(amount)
    except ValueError:
        return jsonify({
            "error": "Amount must be a number"
        }), 400

    if amount <= 0:
        return jsonify({
            "error": "Amount must be greater than zero"
        }), 400

    result = transfer_money(sender, receiver, amount)

    if "error" in result:
        return jsonify({
            "error": result["error"]
        }), result.get("status", 400)

    return jsonify(result), 200


@transfer_bp.route("/transactions", methods=["GET"])
def transactions():

    transactions = get_all_transactions()

    result = []

    for transaction in transactions:

        result.append({

            "transaction_id": str(transaction[1]),
            "sender": transaction[2],
            "receiver": transaction[3],
            "amount": float(transaction[4]),
            "status": transaction[5],
            "created_at": str(transaction[6])

        })

    return jsonify(result), 200


@transfer_bp.route("/transaction/<transaction_id>", methods=["GET"])
def transaction(transaction_id):

    tx = get_transaction(transaction_id)

    if tx is None:
        return jsonify({"message": "Transaction not found"}), 404

    return jsonify(tx)