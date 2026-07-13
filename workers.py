from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
import schemas
import crud
from database import get_db

router = APIRouter(prefix="/api/workers", tags=["Workers"])

@router.post("/", response_model=schemas.Worker)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):
    """Create a new worker"""
    existing = crud.WorkerCRUD.get_worker_by_worker_id(db, worker.worker_id)
    if existing:
        raise HTTPException(status_code=400, detail="Worker ID already exists")
    return crud.WorkerCRUD.create_worker(db, worker)

@router.get("/", response_model=List[schemas.Worker])
def get_workers(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    active_only: bool = True,
    db: Session = Depends(get_db)
):
    """Get all workers"""
    return crud.WorkerCRUD.get_workers(db, skip, limit, active_only)

@router.get("/{worker_id}", response_model=schemas.Worker)
def get_worker(worker_id: int, db: Session = Depends(get_db)):
    """Get a specific worker by ID"""
    worker = crud.WorkerCRUD.get_worker(db, worker_id)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker

@router.get("/by-worker-id/{worker_code}", response_model=schemas.Worker)
def get_worker_by_code(worker_code: str, db: Session = Depends(get_db)):
    """Get a specific worker by their unique worker code"""
    worker = crud.WorkerCRUD.get_worker_by_worker_id(db, worker_code)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker

@router.put("/{worker_id}", response_model=schemas.Worker)
def update_worker(
    worker_id: int, 
    worker_update: schemas.WorkerUpdate, 
    db: Session = Depends(get_db)
):
    """Update a specific worker"""
    worker = crud.WorkerCRUD.update_worker(db, worker_id, worker_update)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker

@router.delete("/{worker_id}")
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    """Delete a specific worker"""
    success = crud.WorkerCRUD.delete_worker(db, worker_id)
    if not success:
        raise HTTPException(status_code=404, detail="Worker not found")
    return {"message": "Worker deleted successfully"}