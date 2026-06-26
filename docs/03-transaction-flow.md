# Transaction Flow

1. User submits payment request.

2. API Gateway receives request.

3. Payment Service validates sender and receiver.

4. Payment Service publishes the event to Apache Kafka.

5. Transaction Processing Service consumes the event.

6. Transaction is stored in PostgreSQL.

7. Redis cache is updated.

8. Notification Service sends confirmation.

9. API returns SUCCESS response.
