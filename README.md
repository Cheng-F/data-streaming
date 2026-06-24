# Data Streaming

DE Zoomcamp 2026 - Module 7: Streaming with Kafka (Redpanda) and PyFlink.

## Setup

```bash
docker compose build
docker compose up -d
```

Services:
- Redpanda (Kafka-compatible) on `localhost:9092`
- Flink Job Manager at http://localhost:8081
- PostgreSQL on `localhost:5432`

## Usage

**Create Kafka topic and send data (Q2):**
```bash
docker exec -it streaming-redpanda-1 rpk topic create green-trips
python src/producer.py
```

**Count trips with distance > 5 km (Q3):**
```bash
python src/consumer.py
```

**Create PostgreSQL tables:**
```bash
docker exec -i streaming-postgres-1 psql -U postgres -d postgres < create_tables.sql
```

**Run Flink jobs (Q4–Q6):**
```bash
docker exec -it streaming-jobmanager-1 flink run -py /opt/src/job/q4_tumbling_window.py
docker exec -it streaming-jobmanager-1 flink run -py /opt/src/job/q5_session_window.py
docker exec -it streaming-jobmanager-1 flink run -py /opt/src/job/q6_tip_amount.py
```

## Data

Green Taxi Trip data, October 2025:
https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-10.parquet
