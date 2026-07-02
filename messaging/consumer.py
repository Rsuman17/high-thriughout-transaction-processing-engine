from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "payment-events",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Kafka Consumer Started...\n")

for message in consumer:

    print("Received Event")

    print(message.value)