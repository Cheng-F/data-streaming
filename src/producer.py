import json
import pandas as pd
from kafka import KafkaProducer
from time import time

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-10.parquet"
COLUMNS = [
    'lpep_pickup_datetime',
    'lpep_dropoff_datetime',
    'PULocationID',
    'DOLocationID',
    'passenger_count',
    'trip_distance',
    'tip_amount',
    'total_amount',
]
TOPIC = 'green-trips'

df = pd.read_parquet(URL, columns=COLUMNS)
print(f"Loaded {len(df)} rows")

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

t0 = time()

for _, row in df.iterrows():
    record = {
        'lpep_pickup_datetime': str(row['lpep_pickup_datetime']),
        'lpep_dropoff_datetime': str(row['lpep_dropoff_datetime']),
        'PULocationID': int(row['PULocationID']),
        'DOLocationID': int(row['DOLocationID']),
        'passenger_count': float(row['passenger_count']) if pd.notna(row['passenger_count']) else None,
        'trip_distance': float(row['trip_distance']),
        'tip_amount': float(row['tip_amount']),
        'total_amount': float(row['total_amount']),
    }
    producer.send(TOPIC, value=record)

producer.flush()

t1 = time()
print(f'took {(t1 - t0):.2f} seconds')
