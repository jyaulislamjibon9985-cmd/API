from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from database import Base

class ViolationType(enum.Enum):
    NO_HELMET = "no_helmet"
    NO_VEST = "no_vest"
    RESTRICTED_AREA = "restricted_area"
    UNSAFE_BEHAVIOR = "unsafe_behavior"

class IncidentStatus(enum.Enum):
    PENDING = "pending"
    REVIEWED = "reviewed"
    RESOLVED = "resolved"
    DISMISSED = "dismissed"

class Worker(Base):
    __tablename__ = "workers"
    
    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    department = Column(String(100))
    shift = Column(String(50))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    incidents = relationship("Incident", back_populates="worker")
    equipment_records = relationship("SafetyEquipmentRecord", back_populates="worker")
    safety_equipment = relationship("SafetyEquipment", back_populates="worker")

class SafetyEquipment(Base):
    __tablename__ = "safety_equipment"
    
    id = Column(Integer, primary_key=True, index=True)
    equipment_type = Column(String(50), nullable=False)  # helmet, vest, gloves, etc.
    equipment_id = Column(String(50), unique=True, nullable=False)
    is_required = Column(Boolean, default=True)
    is_functional = Column(Boolean, default=True)
    assigned_to = Column(Integer, ForeignKey("workers.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    worker = relationship("Worker", back_populates="safety_equipment")
    equipment_records = relationship("SafetyEquipmentRecord", back_populates="equipment")

class RestrictedZone(Base):
    __tablename__ = "restricted_zones"
    
    id = Column(Integer, primary_key=True, index=True)
    zone_name = Column(String(100), nullable=False)
    zone_code = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    coordinates = Column(Text)  # JSON string of zone coordinates
    risk_level = Column(String(20))  # high, medium, low
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    incidents = relationship("Incident", back_populates="zone")

class Incident(Base):
    __tablename__ = "incidents"
    
    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(String(50), unique=True, nullable=False)
    violation_type = Column(Enum(ViolationType), nullable=False)
    worker_id = Column(Integer, ForeignKey("workers.id"), nullable=True)
    zone_id = Column(Integer, ForeignKey("restricted_zones.id"), nullable=True)
    camera_id = Column(String(50))
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.PENDING)
    description = Column(Text)
    image_url = Column(String(255))
    video_url = Column(String(255))
    severity_score = Column(Float, default=1.0)
    reviewed_by = Column(String(100))
    reviewed_at = Column(DateTime)
    resolved_at = Column(DateTime)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    worker = relationship("Worker", back_populates="incidents")
    zone = relationship("RestrictedZone", back_populates="incidents")

class SafetyEquipmentRecord(Base):
    __tablename__ = "safety_equipment_records"
    
    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("workers.id"), nullable=False)
    equipment_id = Column(Integer, ForeignKey("safety_equipment.id"), nullable=False)
    is_wearing = Column(Boolean, default=False)
    detection_timestamp = Column(DateTime, default=datetime.utcnow)
    camera_id = Column(String(50))
    confidence_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    worker = relationship("Worker", back_populates="equipment_records")
    equipment = relationship("SafetyEquipment", back_populates="equipment_records")