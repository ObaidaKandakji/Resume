# Project Spec: AKS Store Platform

## Resume Title

AKS Store Platform (Infrastructure & Deployment Layer)

## Repositories / Links

- https://github.com/ObaidaKandakji/Distributed-E-Commerce-Microservices-Platform

## Project Type

Cloud-native microservices deployment platform (Kubernetes infrastructure + CI/CD workflow template).

## Problem It Solves

Provides a single deployment layer for a multi-service e-commerce system so services and stateful dependencies can run together on AKS.
Defines a repeatable CI/CD pattern to build, release, and roll out container images to Kubernetes.
Supports asynchronous order processing architecture via RabbitMQ-backed service wiring.

## What Was Actually Built

- A consolidated Kubernetes manifest (`Deployment Files/aps-all-in-one.yaml`) containing:
  - 1 `ConfigMap` for RabbitMQ plugins
  - 2 `StatefulSet` resources (`mongodb`, `rabbitmq`)
  - 5 application `Deployment` resources (`order-service`, `makeline-service`, `product-service`, `store-front`, `store-admin`)
  - 7 `Service` resources (internal + external)
- Service runtime wiring through environment variables (queue host/port/name, DB URI/name/collection, inter-service URLs).
- Health checks (`startupProbe`, `readinessProbe`, `livenessProbe`) across multiple deployments.
- A reusable GitHub Actions workflow template (`Deployment Files/ci_cd.yaml`) with `Build`, `Test`, `Release`, and `Deploy` jobs.
- Architecture and deployment documentation in `README.md`, plus architecture diagram (`BestBuyarchitecture.png`).

## Tech Stack (Verified)

- Kubernetes manifests (Deployments, StatefulSets, Services, ConfigMap)
- GitHub Actions
- Docker / Docker Hub image workflow
- Azure Kubernetes Service (AKS) deployment target (documented)
- RabbitMQ (`rabbitmq:3-management`)
- MongoDB (`mongo:4.2`)
- `kubectl` and Azure CLI commands (documented)
- YAML and Markdown

## Allowed Keywords (With Evidence)

- `Kubernetes`: `Deployment Files/aps-all-in-one.yaml` defines Deployments, StatefulSets, Services, and ConfigMap.
- `AKS`: `README.md` title/sections explicitly describe deployment to Azure Kubernetes Service.
- `CI/CD`: `Deployment Files/ci_cd.yaml` includes Build, Test, Release, Deploy jobs.
- `GitHub Actions`: workflow file is implemented in `Deployment Files/ci_cd.yaml`.
- `Docker`: workflow builds/pushes images and promotes tags in `Deployment Files/ci_cd.yaml`.
- `Microservices`: `README.md` service breakdown lists separate storefront/admin/API/processing services.
- `Event-driven architecture`: `README.md` system flow describes orders published to RabbitMQ and consumed asynchronously.
- `RabbitMQ`: declared as StatefulSet/Service in `Deployment Files/aps-all-in-one.yaml`.
- `MongoDB`: declared as StatefulSet/Service with persistent volume claim in `Deployment Files/aps-all-in-one.yaml`.
- `LoadBalancer services`: `store-front` and `store-admin` services use `type: LoadBalancer` in `Deployment Files/aps-all-in-one.yaml`.
- `Health probes`: multiple deployments define startup/readiness/liveness probes in `Deployment Files/aps-all-in-one.yaml`.
- `Container orchestration`: manifests + rollout commands in README/workflow show orchestrated deployment behavior.

## Do Not Claim

- Do not claim real unit/integration test execution or test coverage percentages; workflow test steps are simulated `echo` commands.
- Do not claim production traffic, revenue, latency, throughput, or error-rate improvements (UNVERIFIED).
- Do not claim autoscaling, multi-region, zero-downtime guarantees, or high-availability architecture beyond what is explicitly declared.
- Do not claim hardened secret management; default RabbitMQ username/password values are present in manifest env vars.
- Do not claim the optional AI integration path is fully implemented in this repository (only an `AI_SERVICE_URL` reference is present).

## Metrics / Outcomes

- 15 Kubernetes resources defined in one manifest (`Deployment Files/aps-all-in-one.yaml`): 1 ConfigMap, 2 StatefulSets, 5 Deployments, 7 Services.
- 2 externally exposed frontend endpoints defined via `LoadBalancer` services (`store-front`, `store-admin`).
- 4-stage CI/CD workflow template implemented (`Build`, `Test`, `Release`, `Deploy`).
- Workflow includes image promotion flow from `:test` to `:latest` before deployment.
- Runtime performance metrics (latency/throughput/error rate): UNVERIFIED.
- Production deployment frequency and success rate: UNVERIFIED.

## Quantification Candidates

- User-confirmed estimate: `~90%` reduction in manual deployment effort per release
  - Basis: CI/CD replaced repeated manual build, push, and rollout steps across 5 services.

## Best-Fit Job Signals

- Kubernetes platform engineering
- DevOps / CI-CD pipeline implementation
- Cloud infrastructure on Azure (AKS)
- Microservices deployment architecture
- Event-driven systems (RabbitMQ)
- Containerized application delivery

## Bullet Bank (Truthful Variants)

- Built a single Kubernetes deployment manifest for a multi-service e-commerce platform, defining 15 resources across app, queue, and database layers, so the full stack can be brought up with one apply operation.
- Implemented AKS-ready infrastructure-as-code for five services plus MongoDB and RabbitMQ, resulting in a reproducible deployment baseline for customer and admin workflows.
- Designed service-to-service runtime wiring with explicit environment variables and internal service discovery, enabling decoupled API, queue, and persistence integration in-cluster.
- Added startup, readiness, and liveness probes to application deployments, improving operational clarity by making health and rollout gates explicit in Kubernetes specs.
- Created a GitHub Actions CI/CD template with Build, Test, Release, and Deploy stages that promotes Docker images from `:test` to `:latest` before Kubernetes rollout.
- Configured frontend exposure through two `LoadBalancer` services while keeping backend services on internal networking, balancing public access needs with cluster-internal API boundaries.
- Defined RabbitMQ and MongoDB as StatefulSets with plugin/config and persistent storage configuration, establishing codified stateful infrastructure for asynchronous order handling.
