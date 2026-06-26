# Payment API

## POST /api/v1/payments

Creates a new payment transaction.

### Request

```json
{
  "senderId": "USR1001",
  "receiverId": "USR2001",
  "amount": 500,
  "currency": "INR"
}
```

---

### Success Response

```json
{
  "transactionId": "TXN100001",
  "status": "SUCCESS",
  "message": "Payment processed successfully"
}
```

---

### Failure Response

```json
{
  "status": "FAILED",
  "message": "Insufficient Balance"
}
```
