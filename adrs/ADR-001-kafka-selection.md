# ADR-001: Kafka Selection

## Status

Accepted

## Context

The system must process thousands of transactions per second while ensuring reliability and scalability.

## Decision

Apache Kafka will be used as the event streaming platform.

## Reasons

- High throughput
- Fault tolerance
- Event replay capability
- Horizontal scalability

## Consequences

The system becomes event-driven and can scale efficiently as transaction volume increases.
