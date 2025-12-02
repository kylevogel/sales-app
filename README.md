Sales Performance Dashboard
1) Executive Summary
Problem: Sales teams often struggle to track their daily performance and application reliability in real-time, leading to delayed decision-making and unmonitored system outages.
Solution: This project is a containerized Sales Application that provides an interactive dashboard for tracking sales metrics. We have enhanced the application with a robust observability layer (Logging and Metrics) to ensure system health and performance can be monitored by operations teams.
2) System Overview
Course Concept(s):
Logging & Metrics (Observability): We implemented structured logging to track application lifecycle events and integrated a Prometheus metrics exporter to monitor request counts and system health.
Architecture Diagram:
graph TD
    User((User / Browser))
    
    subgraph "Docker Container (sales-app)"
        App[Main Sales App]
        Logs[Structured Logs]
        Metrics[Prometheus Metrics Server]
    end
    
    User -->|Visits Dashboard (Port 8080)| App
    User -->|Scrapes Metrics (Port 9090)| Metrics
    App -->|Writes| Logs
    App -.->|Increments| Metrics
    Logs -->|Output| StdOut[Docker Console]

Data/Models/Services:
Source: Local sales datasets located in the src/ directory.
Format: Python-based application serving data via HTTP.
License: MIT License (Open Source).


3) How to Run (Local)
This application is containerized using Docker. Follow these steps to build and run the application locally.
Prerequisites:
Docker Desktop installed and running.
Build:
docker build -t sales-app .

Run:
Port 8080: Main Application
Port 9090: Metrics Endpoint
docker run -p 8080:8080 -p 9090:9090 sales-app

Verify:
Dashboard: Navigate to http://localhost:8080 to view the sales app.
Metrics: Navigate to http://localhost:9090 to view the Prometheus metrics data.

4. Design Decisions

Why Logging & Metrics? We prioritized Observability as our core integration. In production environments, knowing that an app is running is not enough; we need to know how it is behaving.

Logging: We utilized Python's standard logging library to ensure that all critical events (startup, errors, access) are printed to stdout. This allows Docker logs to capture them without complex file management.

Metrics: We integrated the prometheus-client library. Instead of building a complex custom dashboard for system stats, we exposed a standard /metrics endpoint. This allows industry-standard tools (like Prometheus/Grafana) to scrape our app without us writing custom visualization code.

Tradeoffs:
Complexity vs. Utility: Running a separate metrics server on port 9090 adds slight complexity to the networking (requiring two ports to be exposed). However, this separates "User Traffic" from "Ops Traffic," which is a security best practice.
Storage: We are currently using ephemeral local storage for the application state. For a larger scale, we would migrate to a dedicated database (PostgreSQL).

Ops:
Monitoring: The application now self-reports its health. If the container crashes or restarts, the app_startups_total metric will reveal instability immediately.

5. Results & Evaluation

Functionality Check: The application successfully builds and serves traffic. The observability layer is active and reporting data.
Performance: The metrics server is lightweight and runs on a separate thread, ensuring zero impact on the main dashboard's loading speed.

6. What's Next

Grafana Integration: Connect the port 9090 output to a Grafana dashboard for historical visualization.
Alerting: Add logic to trigger alerts if error rates spike.

7. Links

GitHub Repo: https://github.com/aelias5438/sales-app
Public Cloud App: https://kylev3-sales-app.azurewebsites.net/
