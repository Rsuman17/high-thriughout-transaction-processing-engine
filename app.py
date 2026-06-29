from flask import Flask
from routes.health import health_bp
from routes.payment import payment_bp

app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(payment_bp)

@app.route("/")
def home():
    return "High Throughput Transaction Processing Engine"

if __name__ == "__main__":
    app.run(debug=True)