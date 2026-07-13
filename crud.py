from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc
from datetime import datetime
from typing import Optional, List
import models
import schemas

# Worker CRUD
class WorkerCRUD:
    @staticmethod
    def create_worker(db: Session, worker: schemas.WorkerCreate):
        db_worker = models.Worker(**worker.model_dump())
        db.add(db_worker)
        db.commit()
        db.refresh(db_worker)
        return db_worker
    
    @staticmethod
    def get_worker(db: Session, worker_id: int):
        return db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    
    @staticmethod
    def get_worker_by_worker_id(db: Session, worker_id: str):
        return db.query(models.Worker).filter(models.Worker.worker_id == worker_id).first()
    
    @staticmethod
    def get_workers(db: Session, skip: int = 0, limit: int = 100, active_only: bool = True):
        query = db.query(models.Worker)
        if active_only:
            query = query.filter(models.Worker.is_active == True)
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def update_worker(db: Session, worker_id: int, worker_update: schemas.WorkerUpdate):
        db_worker = WorkerCRUD.get_worker(db, worker_id)
        if db_worker:
            update_data = worker_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_worker, key, value)
            db_worker.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(db_worker)
        return db_worker
    
    @staticmethod
    def delete_worker(db: Session, worker_id: int):
        db_worker = WorkerCRUD.get_worker(db, worker_id)
        if db_worker:
            db.delete(db_worker)
            db.commit()
            return True
        return False

# Incident CRUD
class IncidentCRUD:
    @staticmethod
    def create_incident(db: Session, incident: schemas.IncidentCreate):
        db_incident = models.Incident(**incident.model_dump())
        db.add(db_incident)
        db.commit()
        db.refresh(db_incident)
        return db_incident
    
    @staticmethod
    def get_incident(db: Session, incident_id: int):
        return db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    
    @staticmethod
    def get_incident_by_incident_id(db: Session, incident_code: str):
        return db.query(models.Incident).filter(models.Incident.incident_id == incident_code).first()
    
    @staticmethod
    def get_incidents(db: Session, skip: int = 0, limit: int = 100, 
                     status: Optional[models.IncidentStatus] = None,
                     violation_type: Optional[models.ViolationType] = None,
                     worker_id: Optional[int] = None):
        query = db.query(models.Incident)
        if status:
            query = query.filter(models.Incident.status == status)
        if violation_type:
            query = query.filter(models.Incident.violation_type == violation_type)
        if worker_id:
            query = query.filter(models.Incident.worker_id == worker_id)
        return query.order_by(desc(models.Incident.created_at)).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_incident(db: Session, incident_id: int, incident_update: schemas.IncidentUpdate):
        db_incident = IncidentCRUD.get_incident(db, incident_id)
        if db_incident:
            update_data = incident_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_incident, key, value)
            db_incident.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(db_incident)
        return db_incident
    
    @staticmethod
    def delete_incident(db: Session, incident_id: int):
        db_incident = IncidentCRUD.get_incident(db, incident_id)
        if db_incident:
            db.delete(db_incident)
            db.commit()
            return True
        return False

# Safety Equipment CRUD
class SafetyEquipmentCRUD:
    @staticmethod
    def create_equipment(db: Session, equipment: schemas.SafetyEquipmentCreate):
        db_equipment = models.SafetyEquipment(**equipment.model_dump())
        db.add(db_equipment)
        db.commit()
        db.refresh(db_equipment)
        return db_equipment
    
    @staticmethod
    def get_equipment(db: Session, equipment_id: int):
        return db.query(models.SafetyEquipment).filter(models.SafetyEquipment.id == equipment_id).first()
    
    @staticmethod
    def get_equipment_by_code(db: Session, equipment_code: str):
        return db.query(models.SafetyEquipment).filter(models.SafetyEquipment.equipment_id == equipment_code).first()
    
    @staticmethod
    def get_all_equipment(db: Session, skip: int = 0, limit: int = 100, functional_only: bool = False):
        query = db.query(models.SafetyEquipment)
        if functional_only:
            query = query.filter(models.SafetyEquipment.is_functional == True)
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def update_equipment(db: Session, equipment_id: int, equipment_update: schemas.SafetyEquipmentUpdate):
        db_equipment = SafetyEquipmentCRUD.get_equipment(db, equipment_id)
        if db_equipment:
            update_data = equipment_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_equipment, key, value)
            db_equipment.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(db_equipment)
        return db_equipment
    
    @staticmethod
    def delete_equipment(db: Session, equipment_id: int):
        db_equipment = SafetyEquipmentCRUD.get_equipment(db, equipment_id)
        if db_equipment:
            db.delete(db_equipment)
            db.commit()
            return True
        return False

# Restricted Zone CRUD
class RestrictedZoneCRUD:
    @staticmethod
    def create_zone(db: Session, zone: schemas.RestrictedZoneCreate):
        db_zone = models.RestrictedZone(**zone.model_dump())
        db.add(db_zone)
        db.commit()
        db.refresh(db_zone)
        return db_zone
    
    @staticmethod
    def get_zone(db: Session, zone_id: int):
        return db.query(models.RestrictedZone).filter(models.RestrictedZone.id == zone_id).first()
    
    @staticmethod
    def get_zone_by_code(db: Session, zone_code: str):
        return db.query(models.RestrictedZone).filter(models.RestrictedZone.zone_code == zone_code).first()
    
    @staticmethod
    def get_all_zones(db: Session, skip: int = 0, limit: int = 100, active_only: bool = True):
        query = db.query(models.RestrictedZone)
        if active_only:
            query = query.filter(models.RestrictedZone.is_active == True)
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def update_zone(db: Session, zone_id: int, zone_update: schemas.RestrictedZoneUpdate):
        db_zone = RestrictedZoneCRUD.get_zone(db, zone_id)
        if db_zone:
            update_data = zone_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_zone, key, value)
            db_zone.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(db_zone)
        return db_zone
    
    @staticmethod
    def delete_zone(db: Session, zone_id: int):
        db_zone = RestrictedZoneCRUD.get_zone(db, zone_id)
        if db_zone:
            db.delete(db_zone)
            db.commit()
            return True
        return False

# Equipment Record CRUD
class EquipmentRecordCRUD:
    @staticmethod
    def create_record(db: Session, record: schemas.SafetyEquipmentRecordCreate):
        db_record = models.SafetyEquipmentRecord(**record.model_dump())
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        return db_record
    
    @staticmethod
    def get_record(db: Session, record_id: int):
        return db.query(models.SafetyEquipmentRecord).filter(models.SafetyEquipmentRecord.id == record_id).first()
    
    @staticmethod
    def get_records_by_worker(db: Session, worker_id: int, skip: int = 0, limit: int = 100):
        return db.query(models.SafetyEquipmentRecord).filter(
            models.SafetyEquipmentRecord.worker_id == worker_id
        ).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_all_records(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.SafetyEquipmentRecord).order_by(
            desc(models.SafetyEquipmentRecord.detection_timestamp)
        ).offset(skip).limit(limit).all()
    
    @staticmethod
    def delete_record(db: Session, record_id: int):
        db_record = EquipmentRecordCRUD.get_record(db, record_id)
        if db_record:
            db.delete(db_record)
            db.commit()
            return True
        return False
