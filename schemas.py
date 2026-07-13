from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from enum import Enum

class ViolationType(str, Enum):
    NO_HELMET = "no_helmet"
    NO_VEST = "no_vest"
    RESTRICTED_AREA = "restricted_area"
    UNSAFE_BEHAVIOR = "unsafe_behavior"

class IncidentStatus(str, Enum):
    PENDING = "pending"
    REVIEWED = "reviewed"
    RESOLVED = "resolved"
    DISMISSED = "dismissed"

# Worker Schemas
class WorkerBase(BaseModel):
    worker_id: str
    name: str
    department: Optional[str] = None
    shift: Optional[str] = None
    is_active: Optional[bool] = True

class WorkerCreate(WorkerBase):
    pass

class WorkerUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    shift: Optional[str] = None
    is_active: Optional[bool] = None

class Worker(WorkerBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Safety Equipment Schemas
class SafetyEquipmentBase(BaseModel):
    equipment_type: str
    equipment_id: str
    is_required: Optional[bool] = True
    is_functional: Optional[bool] = True
    assigned_to: Optional[int] = None

class SafetyEquipmentCreate(SafetyEquipmentBase):
    pass

class SafetyEquipmentUpdate(BaseModel):
    equipment_type: Optional[str] = None
    is_required: Optional[bool] = None
    is_functional: Optional[bool] = None
    assigned_to: Optional[int] = None

class SafetyEquipment(SafetyEquipmentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Restricted Zone Schemas
class RestrictedZoneBase(BaseModel):
    zone_name: str
    zone_code: str
    description: Optional[str] = None
    coordinates: Optional[str] = None
    risk_level: Optional[str] = None
    is_active: Optional[bool] = True

class RestrictedZoneCreate(RestrictedZoneBase):
    pass

class RestrictedZoneUpdate(BaseModel):
    zone_name: Optional[str] = None
    description: Optional[str] = None
    coordinates: Optional[str] = None
    risk_level: Optional[str] = None
    is_active: Optional[bool] = None

class RestrictedZone(RestrictedZoneBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Incident Schemas
class IncidentBase(BaseModel):
    incident_id: str
    violation_type: ViolationType
    worker_id: Optional[int] = None
    zone_id: Optional[int] = None
    camera_id: Optional[str] = None
    timestamp: Optional[datetime] = None
    status: Optional[IncidentStatus] = IncidentStatus.PENDING
    description: Optional[str] = None
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    severity_score: Optional[float] = 1.0
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    notes: Optional[str] = None

class IncidentCreate(IncidentBase):
    pass

class IncidentUpdate(BaseModel):
    status: Optional[IncidentStatus] = None
    description: Optional[str] = None
    severity_score: Optional[float] = None
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    notes: Optional[str] = None
    image_url: Optional[str] = None
    video_url: Optional[str] = None

class Incident(IncidentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    worker: Optional[Worker] = None
    zone: Optional[RestrictedZone] = None
    
    class Config:
        from_attributes = True

# Safety Equipment Record Schemas
class SafetyEquipmentRecordBase(BaseModel):
    worker_id: int
    equipment_id: int
    is_wearing: bool
    camera_id: Optional[str] = None
    confidence_score: Optional[float] = None

class SafetyEquipmentRecordCreate(SafetyEquipmentRecordBase):
    pass

class SafetyEquipmentRecord(SafetyEquipmentRecordBase):
    id: int
    detection_timestamp: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True