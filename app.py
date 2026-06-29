from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)