from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime
import schemas
import crud
from database import get_db

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])

@router.post("/", response_model=schemas.Incident)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    """Create a new safety incident"""
    # Check if incident_id already exists
    existing = crud.IncidentCRUD.get_incident_by_incident_id(db, incident.incident_id)
    if existing:
        raise HTTPException(status_code=400, detail="Incident ID already exists")
    
    return crud.IncidentCRUD.create_incident(db, incident)

@router.get("/", response_model=List[schemas.Incident])
def get_incidents(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    status: Optional[schemas.IncidentStatus] = None,
    violation_type: Optional[schemas.ViolationType] = None,
    worker_id: Optional[int] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    """Get all incidents with optional filters"""
    return crud.IncidentCRUD.get_incidents(
        db, skip, limit, status, violation_type, worker_id, start_date, end_date
    )

@router.get("/{incident_id}", response_model=schemas.Incident)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    """Get a specific incident by ID"""
    incident = crud.IncidentCRUD.get_incident(db, incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.get("/by-incident-id/{incident_code}", response_model=schemas.Incident)
def get_incident_by_code(incident_code: str, db: Session = Depends(get_db)):
    """Get a specific incident by its unique incident code"""
    incident = crud.IncidentCRUD.get_incident_by_incident_id(db, incident_code)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.put("/{incident_id}", response_model=schemas.Incident)
def update_incident(
    incident_id: int, 
    incident_update: schemas.IncidentUpdate, 
    db: Session = Depends(get_db)
):
    """Update a specific incident"""
    incident = crud.IncidentCRUD.update_incident(db, incident_id, incident_update)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.delete("/{incident_id}")
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    """Delete a specific incident"""
    success = crud.IncidentCRUD.delete_incident(db, incident_id)
    if not success:
        raise HTTPException(status_code=404, detail="Incident not found")
    return {"message": "Incident deleted successfully"}

@router.get("/statistics/")
def get_incident_statistics(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    """Get incident statistics"""
    return crud.IncidentCRUD.get_incident_statistics(db, start_date, end_date)