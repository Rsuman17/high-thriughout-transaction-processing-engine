# ADR-002: Database Selection

## Status

Accepted

## Date

2026-06-26

## Context

The High Throughput Transaction Processing Engine must support approximately **12,000 Transactions Per Second (TPS)** while maintaining ACID compliance, high availability, low latency, and horizontal scalability. The database should efficiently handle concurrent financial transactions and scale as the system grows.

## Decision Drivers

* ACID compliance
* Horizontal scalability
* High throughput
* Low latency
* Fault tolerance
* Strong consistency
* Mature ecosystem
* Ease of integration

## Options Considered

### Option 1: PostgreSQL + Citus

**Pros**

* Full ACID compliance
* Horizontally scalable using Citus
* Mature and widely adopted ecosystem
* Excellent SQL support
* Reliable for financial transactions
* Easy integration with Java Spring Boot

**Cons**

* Requires Citus extension for distributed scaling
* Operational complexity increases with cluster size

---

### Option 2: CockroachDB

**Pros**

* Distributed SQL database
* Automatic replication
* Strong consistency
* High availability

**Cons**

* More complex to tune for high-performance workloads
* Smaller community compared to PostgreSQL
* Higher learning curve

---

### Option 3: TiDB

**Pros**

* Excellent horizontal scalability
* MySQL-compatible
* Strong support for large distributed workloads

**Cons**

* More infrastructure components to manage
* Less common in enterprise fintech projects
* Higher operational overhead

---

## Decision

**PostgreSQL + Citus** has been selected as the primary database technology.

## Rationale

PostgreSQL is a proven relational database with excellent support for ACID transactions, making it highly suitable for financial systems. By extending PostgreSQL with Citus, the system gains horizontal scalability while retaining SQL compatibility and transactional reliability.

Compared to CockroachDB and TiDB, PostgreSQL + Citus offers a strong balance between performance, maturity, scalability, and ease of development. It also integrates seamlessly with the selected application stack and supports future scaling requirements.

## Consequences

### Advantages

* Reliable ACID transactions
* Horizontal scaling through sharding
* Mature ecosystem and extensive documentation
* Excellent performance for transactional workloads
* Easier onboarding for developers

### Disadvantages

* Distributed cluster management requires additional operational effort
* Citus introduces some administrative complexity

## Final Decision

PostgreSQL + Citus provides the best combination of transactional reliability, scalability, performance, and maintainability for a high-throughput transaction processing engine targeting **12,000 TPS**.
