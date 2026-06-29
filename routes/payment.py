from flask import Blueprint, request, jsonify
import uuid

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/payment", methods=["POST"])
def payment():

    data = request.get_json()

    transaction_id = str(uuid.uuid4())

    return jsonify({
        "transaction_id": transaction_id,
        "status": "SUCCESS",
        "sender": data["sender"],
        "receiver": data["receiver"],
        "amount": data["amount"]
    }), 201