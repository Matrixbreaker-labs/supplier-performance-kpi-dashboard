# Supplier Performance Dashboard & Vendor KPI Engine

A production-grade supply chain data engineering pipeline built using Python async patterns (`asyncio.gather`) and rigorous Pydantic schemas. This application acts as a centralized dashboard subsystem that concurrently ingests, validates, and refines raw operational logistics tracking records from distinct vendor platforms into standardized procurement scoreboards.

## ⚡ Architectural Implementations

* **High-Throughput Ingestion Mapping:** Orchestrates concurrent connection handles using non-blocking asynchronous calls to extract data pools across scattered vendor portals simultaneously.
* **Dual Core Strategic KPIs:** Autonomously computes mission-critical supply chain efficiency metrics:
  * **On-Time Delivery Rate (OTD %):** Performance tiering validating logistical scheduling parameters.
  * **Quality Rate (%):** Material optimization matrix measuring compliance ratios vs. manufacturing defect volume.
* **Tier Stratification Allocation:** Uses dynamic conditional parameters to assign operations into strict operational categorization segments (`Gold`, `Silver`, `Bronze`).
* **Rigorous Runtime Governance:** Implements conditional field-validation checkpoints using customized Pydantic validators preventing contradictory schema submissions.

## 🛠️ Performance Vector & Tech Stack
- **Asynchronous Data Handling:** Python `asyncio` Runtime Engine
- **Data Guard Architecture:** Pydantic (Model Type Enforcements)
- **Output Artifact:** Production-Ready CSV Scoreboard Target File
