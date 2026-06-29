from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)


@app.route("/")
def home():
    return "High Throughput Transaction Processing Engine"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "Transaction Processing Engine"
    })


@app.route("/payment", methods=["POST"])
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


if __name__ == "__main__":
    app.run(debug=True)