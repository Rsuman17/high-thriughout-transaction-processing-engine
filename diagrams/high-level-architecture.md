# High Level Architecture

User
  |
  v
Load Balancer
  |
  v
API Gateway
  |
  +----------------+
  |                |
  v                v
Payment Service   P2P Service
  |                |
  +-------+--------+
          |
          v
       Kafka
          |
          v
Transaction Processor
          |
    +-----+-----+
    |           |
    v           v
 Redis      PostgreSQL
