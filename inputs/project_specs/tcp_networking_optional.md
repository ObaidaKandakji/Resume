# Project Spec: Rideau Canal Skateway Real-Time Monitoring System

## Resume Title

Rideau Canal Skateway Real-Time Monitoring System

## Repositories / Links

- https://github.com/ObaidaKandakji/cst8916-final-project
- https://github.com/ObaidaKandakji/rideau-canal-sensor-simulation
- https://github.com/ObaidaKandakji/rideau-canal-dashboard
- https://cst8916final-f9d7akcqbebqbcam.canadacentral-01.azurewebsites.net/

## Project Type

IoT real-time data pipeline with cloud analytics and web dashboard integration.

## Problem It Solves

Manual checks of Rideau Canal skating conditions are slow and not real-time.  
The project centralizes simulated ice/weather telemetry, processes it continuously, and surfaces safety status for each location.

## What Was Actually Built

- A Stream Analytics query that performs 5-minute tumbling-window aggregations by device/location (`stream-analytics/query.sql`).
- Safety-status classification logic (`Safe`, `Caution`, `Unsafe`) based on ice thickness and surface temperature thresholds (`stream-analytics/query.sql`).
- Dual stream outputs from the same query into Cosmos DB (`SensorAggregations`) and Blob Storage (`historical-data`) (`stream-analytics/query.sql`).
- Project documentation covering architecture, setup, and evidence screenshots (`README.md`, `LINKS.md`, `architecture/`, `screenshots/`).
- Links to companion repositories for the sensor simulator and dashboard (`README.md`, `LINKS.md`).

## Tech Stack (Verified)

- Azure Stream Analytics (SQL query)
- SQL (Stream Analytics query language)
- Azure IoT Hub (documented input source)
- Azure Cosmos DB (documented output target)
- Azure Blob Storage (documented output target)
- Azure App Service (documented dashboard host)
- Markdown documentation (`README.md`, `LINKS.md`)

## Allowed Keywords (With Evidence)

- `Azure Stream Analytics`: Query file defines tumbling-window job and outputs (`stream-analytics/query.sql`).
- `Tumbling Window`: `TumblingWindow(minute, 5)` in query (`stream-analytics/query.sql`).
- `IoT Telemetry Processing`: Input stream `[CST8916Final]` grouped by device and location (`stream-analytics/query.sql`).
- `Real-Time Aggregation`: AVG/MIN/MAX/COUNT calculations in streaming query (`stream-analytics/query.sql`).
- `Safety Classification`: CASE logic outputs `Safe/Caution/Unsafe` (`stream-analytics/query.sql`).
- `Azure Cosmos DB`: Output sink `[SensorAggregations]` and setup details (`stream-analytics/query.sql`, `README.md`).
- `Azure Blob Storage`: Output sink `[historical-data]` and archive description (`stream-analytics/query.sql`, `README.md`).
- `IoT Architecture Documentation`: Diagram and screenshot artifacts (`architecture/architecture.png`, `screenshots/*.png`, `README.md`).
- `Node.js Dashboard Integration`: Documented as companion repo and App Service deployment (`README.md`, `LINKS.md`).
- `Python Sensor Simulation`: Documented as companion repo sending telemetry every 10s (`README.md`, `LINKS.md`).

## Do Not Claim

- Do not claim machine learning, forecasting, or anomaly-detection models.
- Do not claim edge/embedded firmware development in this repository.
- Do not claim load-testing, benchmarking, or production SLO/SLA results.
- Do not claim security hardening/compliance work (for example SOC 2, ISO 27001) without separate evidence.

## Metrics / Outcomes

- Implemented 5-minute windowed aggregation with per-location reading counts and derived safety status (`stream-analytics/query.sql`).
- Configured one analytics flow to persist identical records to two destinations (Cosmos DB + Blob Storage) (`stream-analytics/query.sql`).
- Expected ~30 readings per 5-minute window when telemetry is emitted every 10 seconds: `UNVERIFIED` (`README.md`).
- "Near real-time" responsiveness and "very fast" queries are described qualitatively, but not benchmarked: `UNVERIFIED` (`README.md`).

## Quantification Candidates

- User-confirmed estimate: `~97%` faster monitoring refresh time versus periodic manual review
  - Basis: automated 5-minute windows surface status changes far more frequently than slower manual review cycles.
- User-confirmed estimate: `~27%` reduction in downstream data-handling effort
  - Basis: one analytics job writes both operational and historical outputs without separate export paths.

## Best-Fit Job Signals

- IoT and telemetry data pipelines
- Stream processing and windowed analytics
- Azure cloud data services integration
- Backend/data modeling for operational dashboards
- System architecture documentation and reproducibility

## Bullet Bank (Truthful Variants)

- Replaced manual Rideau Canal condition checks with a streaming analytics pipeline by writing a 5-minute tumbling-window query that converts raw sensor telemetry into location-level safety status records.
- Built Stream Analytics logic that computes AVG/MIN/MAX metrics and reading counts by device/location, giving the dashboard structured, safety-focused aggregates instead of raw events.
- Implemented dual-output stream processing to Cosmos DB and Blob Storage from one query, enabling both operational querying and historical archive capture in the same pipeline.
- Added deterministic output shaping (`id`, `windowEnd`, and safety fields) in the analytics layer, improving downstream consistency for dashboard/API consumption.
- Produced end-to-end architecture and execution evidence (diagram plus Azure/dashboard screenshots), making the IoT pipeline reproducible for reviewers and teammates.
- Connected three related repos (documentation, simulator, dashboard) with setup/deployment guidance, reducing project handoff friction and clarifying component boundaries.
