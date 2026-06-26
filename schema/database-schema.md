# Database Schema

## Users Table

| Column | Type |
|---------|------|
| user_id | UUID |
| name | VARCHAR |
| email | VARCHAR |
| balance | DECIMAL |

---

## Transactions Table

| Column | Type |
|---------|------|
| transaction_id | UUID |
| sender_id | UUID |
| receiver_id | UUID |
| amount | DECIMAL |
| status | VARCHAR |
| created_at | TIMESTAMP |

---

## Notifications Table

| Column | Type |
|---------|------|
| notification_id | UUID |
| transaction_id | UUID |
| user_id | UUID |
| message | TEXT |
| sent_at | TIMESTAMP |
