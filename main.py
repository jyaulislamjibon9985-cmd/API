from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from database import engine, Base
import incidents
import workers
import safety_equipment
import restricted_zones
import equipment_records

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Industrial Safety Monitoring API",
    description="API for monitoring workplace safety using AI and Computer Vision",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Include routers
app.include_router(incidents.router)
app.include_router(workers.router)
app.include_router(safety_equipment.router)
app.include_router(restricted_zones.router)
app.include_router(equipment_records.router)

@app.get("/")
def root():
    return FileResponse("frontend/index.html")

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}