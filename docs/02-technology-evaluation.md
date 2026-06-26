# Technology Evaluation

## API Gateway

Technology: NGINX

Why:
- Request routing
- Rate limiting
- High performance

## Database

Technology: PostgreSQL

Why:
- ACID compliance
- Strong consistency
- Reliable transactions

## Cache

Technology: Redis

Why:
- Fast reads
- Low latency
- Reduces database load

## Event Streaming

Technology: Apache Kafka

Why:
- High throughput
- Fault tolerance
- Event-driven architecture

## Load Balancer

Technology: NGINX

Why:
- Traffic distribution
- High availability
- Scalability

## Conclusion

The selected technology stack can support a fintech transaction processing engine handling 12,000 TPS with low latency and high availability.

## Compare between postgreSQL + cictus vs CockroachDB vs TitaniumDB

| Technology         | Performance | Scalability | Ease of Use | Best Use Case             | Decision     |
| ------------------ | ----------- | ----------- | ----------- | ------------------------- | ------------ |
| PostgreSQL + Citus | High        | Excellent   | Moderate    | Distributed SQL           | ✅ Selected   |
| CockroachDB        | High        | Excellent   | Moderate    | Geo-distributed databases | Not Selected |
| TiDB               | High        | Excellent   | Moderate    | HTAP workloads            | Not Selected |

### Why PostgreSQL + Citus?

Strong PostgreSQL ecosystem.
Horizontal scaling with Citus.
Good support for financial transactions.
Easier integration with Java/Spring Boot than the alternatives.
Suitable for the project's throughput target.

## Message Queue Evaluation

| Technology   | Performance | Scalability | Ease of Use | Best Use Case                                           | Decision     |
| ------------ | ----------- | ----------- | ----------- | ------------------------------------------------------- | ------------ |
| Apache Kafka | Very High   | Excellent   | Moderate    | High-throughput event streaming, financial transactions | ✅ Selected   |
| RabbitMQ     | High        | Good        | Easy        | Task queues, request-response messaging                 | Not Selected |
| Amazon SQS   | Moderate    | Excellent   | Easy        | Cloud-native asynchronous messaging                     | Not Selected |

### Why Apache Kafka?

Apache Kafka was selected as the messaging platform because it is designed to handle millions of events with very high throughput and low latency. Kafka provides durable message storage, horizontal scalability, fault tolerance through replication, and event replay capabilities. These features make it highly suitable for a high-throughput transaction processing engine where reliability and scalability are critical.

### Why not RabbitMQ?

RabbitMQ is an excellent message broker for traditional messaging and task queues. It provides flexible routing and supports multiple messaging protocols. However, compared to Kafka, RabbitMQ is generally less suitable for very high event throughput and long-term event storage, which are important requirements for this project.

### Why not Amazon SQS?

Amazon SQS is a fully managed cloud messaging service that offers excellent scalability and minimal operational overhead. However, it is tightly integrated with the AWS ecosystem and provides limited event replay capabilities compared to Kafka. Since this project focuses on designing a scalable, technology-agnostic transaction processing engine, Kafka is a better architectural choice.

### Final Decision

Apache Kafka is selected because it provides the highest throughput, excellent fault tolerance, horizontal scalability, persistent event storage, and supports event-driven architecture, making it the most appropriate message queue for a fintech transaction processing system capable of processing 12,000 TPS.

