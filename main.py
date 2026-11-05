import asyncio
import csv
import json
import random
import time
import nest_asyncio
from pydantic import BaseModel, Field, field_validator

# Enable internal event loop nesting inside interactive notebooks
nest_asyncio.apply()

# ==============================================================
# 1. Core Data Schemas & Vendor KPI Framework (Pydantic Layer)
# ==============================================================
class VendorMetricsModel(BaseModel):
    vendor_id: str
    vendor_name: str
    total_orders: int = Field(..., gt=0)
    on_time_deliveries: int = Field(..., ge=0)
    defective_items: int = Field(..., ge=0)
    total_items_received: int = Field(..., gt=0)
    
    # Custom business validator ensuring operational consistency
    @field_validator('on_time_deliveries')
    def validate_delivery_count(cls, v, info):
        if 'total_orders' in info.data and v > info.data['total_orders']:
            raise ValueError('On-time deliveries cannot exceed total bulk orders scheduled.')
        return v

class VendorScoreboardOutput(BaseModel):
    vendor_id: str
    vendor_name: str
    on_time_delivery_rate: float  # KPI 1: Goal >= 95% Standard
    quality_rate: float           # KPI 2: Goal >= 98% Standard
    vendor_tier: str              # Tier Allocation: Gold, Silver, Bronze

# ==============================================================
# 2. Automated Vendor Scraping & Processing Engine (Data Ingestion)
# ==============================================================
async def mock_vendor_portal_scraper(vendor_id: int):
    """
    Simulates scraping or processing raw uncurated logistic endpoints 
    across 5 independent supplier internal data portals.
    """
    await asyncio.sleep(random.uniform(0.1, 0.4))  # Simulated I/O latency
    vendor_names = ["Apex Logistics", "Titan Manufacturing", "Nexus Global Supply", "Horizon Freight", "Delta Matrix Group"]
    
    total_orders = random.randint(50, 500)
    # Introducing controlled variance to benchmark different supplier tiers
    on_time = int(total_orders * random.uniform(0.82, 0.99))
    total_items = total_orders * random.randint(10, 50)
    defective = int(total_items * random.uniform(0.005, 0.04))
    
    return {
        "vendor_id": f"VND-{1000 + vendor_id}",
        "vendor_name": vendor_names[vendor_id],
        "total_orders": total_orders,
        "on_time_deliveries": on_time,
        "defective_items": defective,
        "total_items_received": total_items
    }

# ==============================================================
# 3. KPI Evaluation Pipeline (Business Logic Framework)
# ==============================================================
def process_vendor_kpi_metrics(raw_data: dict) -> VendorScoreboardOutput:
    """
    Validates ingested schemas and evaluates Tier performance rulesets
    """
    # Enforce Pydantic contract layer
    metrics = VendorMetricsModel(**raw_data)
    
    # Calculate Key Performance Indicators (KPIs)
    otd_rate = round((metrics.on_time_deliveries / metrics.total_orders) * 100, 2)
    quality_rate = round(((metrics.total_items_received - metrics.defective_items) / metrics.total_items_received) * 100, 2)
    
    # Operational Tier Classification Allocation Logic
    if otd_rate >= 95.0 and quality_rate >= 98.5:
        tier = "GOLD (Preferred Partner)"
    elif otd_rate >= 88.0 and quality_rate >= 96.0:
        tier = "SILVER (Compliant)"
    else:
        tier = "BRONZE (Under Review / Probation)"
        
    return VendorScoreboardOutput(
        vendor_id=metrics.vendor_id,
        vendor_name=metrics.vendor_name,
        on_time_delivery_rate=otd_rate,
        quality_rate=quality_rate,
        vendor_tier=tier
    )

# ==============================================================
# 4. Dashboard Controller Runtime Ecosystem
# ==============================================================
async def execute_supplier_performance_dashboard_pipeline():
    output_csv = "supplier_performance_scoreboard.csv"
    
    print("\n==================================================================")
    print("🚀 INITIALIZING: SUPPLIER PERFORMANCE DASHBOARD & VENDOR KPI ENGINE")
    print("==================================================================\n")
    
    start_time = time.perf_counter()
    
    # Step 1: Concurrently ingest records across multiple portals using list comprehensions
    print("[📡 INGESTION] Triggering asynchronous extraction across supplier network portals...")
    tasks = [mock_vendor_portal_scraper(i) for i in range(5)]
    raw_vendor_payloads = await asyncio.gather(*tasks)
    print(f"[✔] Successfully scraped and processed {len(raw_vendor_payloads)} supplier datastores.\n")
    
    # Step 2: Loop metrics through validation and evaluate core KPIs
    print("[⚙️ ARCHITECTURE] Parsing payloads through validation and business KPI matrix...")
    scoreboard_results = []
    for payload in raw_vendor_payloads:
        try:
            scorecard = process_vendor_kpi_metrics(payload)
            scoreboard_results.append(scorecard)
            print(f"|-- [📊 KPI COMPILED] {scorecard.vendor_name:<20} | OTD: {scorecard.on_time_delivery_rate:<6}% | Quality: {scorecard.quality_rate:<6}% | Tier: {scorecard.vendor_tier}")
        except ValidationError as e:
            print(f"|-- [❌ CRITICAL VALIDATION ERROR] Dropped supplier record: {e.json()}")

    # Step 3: Stream validated matrix straight to corporate CSV file mapping
    with open(output_csv, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["Vendor ID", "Vendor Name", "On-Time Delivery Rate (%)", "Quality Rate (%)", "Vendor Performance Tier"])
        for record in scoreboard_results:
            writer.writerow([record.vendor_id, record.vendor_name, record.on_time_delivery_rate, record.quality_rate, record.vendor_tier])
            
    print(f"\n[💾 CSV DATASTORE] Performance Scoreboard flushed to disk: {output_csv}")
    print("==================================================================")
    print(f"🎉 SUCCESS! Dashboard analytics compiled in {time.perf_counter() - start_time:.4f} Seconds.")
    print("==================================================================")

if __name__ == "__main__":
    asyncio.run(execute_supplier_performance_dashboard_pipeline())
