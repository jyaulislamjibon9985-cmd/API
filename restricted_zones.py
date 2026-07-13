from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
import schemas
import crud
from database import get_db

router = APIRouter(prefix="/api/restricted-zones", tags=["Restricted Zones"])

# CREATE
@router.post("/", response_model=schemas.RestrictedZone, status_code=201)
def create_zone(zone: schemas.RestrictedZoneCreate, db: Session = Depends(get_db)):
    """Create a new restricted zone"""
    existing = crud.RestrictedZoneCRUD.get_zone_by_code(db, zone.zone_code)
    if existing:
        raise HTTPException(status_code=400, detail="Zone code already exists")
    return crud.RestrictedZoneCRUD.create_zone(db, zone)

# READ
@router.get("/", response_model=List[schemas.RestrictedZone])
def get_zones(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    active_only: bool = True,
    db: Session = Depends(get_db)
):
    """Get all restricted zones with pagination"""
    return crud.RestrictedZoneCRUD.get_all_zones(db, skip, limit, active_only)

@router.get("/{zone_id}", response_model=schemas.RestrictedZone)
def get_zone(zone_id: int, db: Session = Depends(get_db)):
    """Get zone by database ID"""
    zone = crud.RestrictedZoneCRUD.get_zone(db, zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Zone not found")
    return zone

@router.get("/code/{zone_code}", response_model=schemas.RestrictedZone)
def get_zone_by_code(zone_code: str, db: Session = Depends(get_db)):
    """Get zone by zone code"""
    zone = crud.RestrictedZoneCRUD.get_zone_by_code(db, zone_code)
    if not zone:
        raise HTTPException(status_code=404, detail="Zone not found")
    return zone

# UPDATE
@router.put("/{zone_id}", response_model=schemas.RestrictedZone)
def update_zone(zone_id: int, zone_update: schemas.RestrictedZoneUpdate, db: Session = Depends(get_db)):
    """Update zone information"""
    zone = crud.RestrictedZoneCRUD.update_zone(db, zone_id, zone_update)
    if not zone:
        raise HTTPException(status_code=404, detail="Zone not found")
    return zone

# DELETE
@router.delete("/{zone_id}", status_code=204)
def delete_zone(zone_id: int, db: Session = Depends(get_db)):
    """Delete a zone"""
    success = crud.RestrictedZoneCRUD.delete_zone(db, zone_id)
    if not success:
        raise HTTPException(status_code=404, detail="Zone not found")
