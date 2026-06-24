import json
from kafka import KafkaConsumer

TOPIC = 'green-trips'

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='green-trips-distance-counter',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=10_000,
)

print(f"Reading all messages from '{TOPIC}'...")

total = 0
count_gt5 = 0

for message in consumer:
    trip = message.value
    total += 1
    if trip['trip_distance'] > 5.0:
        count_gt5 += 1

consumer.close()

print(f"Total trips: {total}")
print(f"Trips with trip_distance > 5.0: {count_gt5}")
