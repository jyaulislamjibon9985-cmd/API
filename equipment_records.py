from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
import schemas
import crud
from database import get_db

router = APIRouter(prefix="/api/equipment-records", tags=["Equipment Records"])

# CREATE
@router.post("/", response_model=schemas.SafetyEquipmentRecord, status_code=201)
def create_record(record: schemas.SafetyEquipmentRecordCreate, db: Session = Depends(get_db)):
    """Create a new equipment detection record"""
    return crud.EquipmentRecordCRUD.create_record(db, record)

# READ
@router.get("/", response_model=List[schemas.SafetyEquipmentRecord])
def get_records(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Get all equipment detection records with pagination"""
    return crud.EquipmentRecordCRUD.get_all_records(db, skip, limit)

@router.get("/{record_id}", response_model=schemas.SafetyEquipmentRecord)
def get_record(record_id: int, db: Session = Depends(get_db)):
    """Get record by database ID"""
    record = crud.EquipmentRecordCRUD.get_record(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

@router.get("/worker/{worker_id}", response_model=List[schemas.SafetyEquipmentRecord])
def get_worker_records(
    worker_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Get all equipment records for a specific worker"""
    return crud.EquipmentRecordCRUD.get_records_by_worker(db, worker_id, skip, limit)

# DELETE
@router.delete("/{record_id}", status_code=204)
def delete_record(record_id: int, db: Session = Depends(get_db)):
    """Delete an equipment record"""
    success = crud.EquipmentRecordCRUD.delete_record(db, record_id)
    if not success:
        raise HTTPException(status_code=404, detail="Record not found")
