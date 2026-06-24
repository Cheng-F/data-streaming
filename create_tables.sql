-- Q4: 5-minute tumbling window counts by pickup location
CREATE TABLE IF NOT EXISTS pickup_location_counts (
    window_start TIMESTAMP,
    "PULocationID" INT,
    num_trips BIGINT,
    PRIMARY KEY (window_start, "PULocationID")
);

-- Q5: Session window results by pickup location
CREATE TABLE IF NOT EXISTS session_window_results (
    "PULocationID" INT,
    session_start TIMESTAMP,
    session_end TIMESTAMP,
    num_trips BIGINT,
    PRIMARY KEY ("PULocationID", session_start)
);

-- Q6: Hourly total tip amounts
CREATE TABLE IF NOT EXISTS hourly_tip_totals (
    window_start TIMESTAMP,
    window_end TIMESTAMP,
    total_tip_amount DOUBLE PRECISION,
    PRIMARY KEY (window_start)
);
