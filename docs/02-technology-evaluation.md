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

Why PostgreSQL + Citus?

Strong PostgreSQL ecosystem.
Horizontal scaling with Citus.
Good support for financial transactions.
Easier integration with Java/Spring Boot than the alternatives.
Suitable for the project's throughput target.
