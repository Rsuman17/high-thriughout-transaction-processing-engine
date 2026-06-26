# Functional Requirements

## Overview

The High-Throughput Transaction Processing Engine (HTTPE) processes digital payment transactions between users. The system validates requests, processes transactions asynchronously using Apache Kafka, stores transaction records, and sends notifications.

---

## Functional Requirements

### FR-1: Accept Payment Request

- The system should accept payment requests from users through the API Gateway.
- Each request should contain sender ID, receiver ID, amount, and transaction ID.

---

### FR-2: Validate Transaction

The system should validate:

- Sender account exists
- Receiver account exists
- Sender has sufficient balance
- Amount is greater than zero

---

### FR-3: Publish Transaction Event

After validation, the Payment Service should publish the transaction event to Apache Kafka.

---

### FR-4: Process Transaction

The Transaction Processing Service should:

- Read messages from Kafka
- Debit sender account
- Credit receiver account
- Store transaction details in PostgreSQL

---

### FR-5: Cache Frequently Used Data

Redis should store frequently accessed data such as account information to reduce database load.

---

### FR-6: Send Notification

After successful processing, the Notification Service should send a success message to both sender and receiver.

---

### FR-7: Handle Failed Transactions

If validation fails or processing encounters an error:

- Reject the transaction
- Log the error
- Return an appropriate failure response

---

## Assumptions

- All APIs use HTTPS.
- Kafka guarantees reliable event delivery.
- PostgreSQL stores permanent transaction records.
- Redis is used only for caching.
