from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

# Paste the ENTIRE contents of q-vercel-latency.json below
TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 212.77,
    "uptime_pct": 97.747,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 137.59,
    "uptime_pct": 98.042,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 185.56,
    "uptime_pct": 97.865,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 224.77,
    "uptime_pct": 97.189,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 142.6,
    "uptime_pct": 98.078,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 166.68,
    "uptime_pct": 98.713,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 201.26,
    "uptime_pct": 98.509,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 193.62,
    "uptime_pct": 99.424,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 214.29,
    "uptime_pct": 98.765,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 173.04,
    "uptime_pct": 98.014,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 156.2,
    "uptime_pct": 99.277,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 107.64,
    "uptime_pct": 99.312,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 210,
    "uptime_pct": 97.988,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 123.05,
    "uptime_pct": 98.083,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 157.33,
    "uptime_pct": 97.785,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 112.43,
    "uptime_pct": 97.233,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 173.08,
    "uptime_pct": 98.481,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 219.1,
    "uptime_pct": 97.348,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 220.24,
    "uptime_pct": 99.438,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 221.7,
    "uptime_pct": 99.427,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 202.04,
    "uptime_pct": 97.103,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 211.98,
    "uptime_pct": 98.81,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 202.94,
    "uptime_pct": 98.179,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 196.01,
    "uptime_pct": 98.946,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 135.14,
    "uptime_pct": 97.309,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 133.27,
    "uptime_pct": 98.805,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 214.43,
    "uptime_pct": 97.507,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 122.22,
    "uptime_pct": 97.905,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 190.01,
    "uptime_pct": 97.196,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 189.43,
    "uptime_pct": 97.438,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 191.9,
    "uptime_pct": 97.985,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 178.03,
    "uptime_pct": 98.456,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 139.17,
    "uptime_pct": 99.124,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 168.56,
    "uptime_pct": 99.494,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 118.08,
    "uptime_pct": 98.056,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 192.01,
    "uptime_pct": 98.676,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()

    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []

    for region in regions:
        records = [r for r in TELEMETRY_DATA if r["region"] == region]

        latencies = [r["latency_ms"] for r in records]
        uptimes = [r["uptime_pct"] for r in records]

        results.append({
            "region": region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime": round(float(np.mean(uptimes)), 3),
            "breaches": int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
