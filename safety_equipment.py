from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
import schemas
import crud
from database import get_db

router = APIRouter(prefix="/api/safety-equipment", tags=["Safety Equipment"])

# CREATE
@router.post("/", response_model=schemas.SafetyEquipment, status_code=201)
def create_equipment(equipment: schemas.SafetyEquipmentCreate, db: Session = Depends(get_db)):
    """Create a new safety equipment entry"""
    existing = crud.SafetyEquipmentCRUD.get_equipment_by_code(db, equipment.equipment_id)
    if existing:
        raise HTTPException(status_code=400, detail="Equipment ID already exists")
    return crud.SafetyEquipmentCRUD.create_equipment(db, equipment)

# READ
@router.get("/", response_model=List[schemas.SafetyEquipment])
def get_equipment(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    functional_only: bool = False,
    db: Session = Depends(get_db)
):
    """Get all safety equipment with pagination"""
    return crud.SafetyEquipmentCRUD.get_all_equipment(db, skip, limit, functional_only)

@router.get("/{equipment_id}", response_model=schemas.SafetyEquipment)
def get_equipment_by_id(equipment_id: int, db: Session = Depends(get_db)):
    """Get equipment by database ID"""
    equipment = crud.SafetyEquipmentCRUD.get_equipment(db, equipment_id)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

@router.get("/code/{equipment_code}", response_model=schemas.SafetyEquipment)
def get_equipment_by_code(equipment_code: str, db: Session = Depends(get_db)):
    """Get equipment by equipment code"""
    equipment = crud.SafetyEquipmentCRUD.get_equipment_by_code(db, equipment_code)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

# UPDATE
@router.put("/{equipment_id}", response_model=schemas.SafetyEquipment)
def update_equipment(equipment_id: int, equipment_update: schemas.SafetyEquipmentUpdate, db: Session = Depends(get_db)):
    """Update equipment information"""
    equipment = crud.SafetyEquipmentCRUD.update_equipment(db, equipment_id, equipment_update)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

# DELETE
@router.delete("/{equipment_id}", status_code=204)
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    """Delete equipment"""
    success = crud.SafetyEquipmentCRUD.delete_equipment(db, equipment_id)
    if not success:
        raise HTTPException(status_code=404, detail="Equipment not found")
