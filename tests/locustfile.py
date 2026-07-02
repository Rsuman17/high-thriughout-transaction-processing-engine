from locust import HttpUser, task, between
import uuid

class PaymentUser(HttpUser):

    wait_time = between(1, 2)

    @task(2)
    def create_payment(self):

        self.client.post(
            "/payment",
            json={
                "sender": "Suman",
                "receiver": "Rahul",
                "amount": 100,
                "idempotency_key": str(uuid.uuid4())
            }
        )

    @task(3)
    def transfer_money(self):

        self.client.post(
            "/transfer",
            json={
                "sender": "Suman",
                "receiver": "Rahul",
                "amount": 50
            }
        )

    @task(1)
    def health(self):

        self.client.get("/health")