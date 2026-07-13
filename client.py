"""
Python Client for Industrial Safety Monitoring API

Usage Example:
    from client import SafetyAPIClient
    
    client = SafetyAPIClient("http://127.0.0.1:8000")
    
    # Create a worker
    worker = client.create_worker("W001", "John Doe", "Manufacturing")
    
    # Get all workers
    workers = client.get_all_workers()
    
    # Create an incident
    incident = client.create_incident("INC001", "no_helmet", worker_id=1)
"""

import requests
import json
from typing import Optional, List, Dict, Any


class SafetyAPIClient:
    """Client for interacting with the Industrial Safety Monitoring API"""
    
    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
    
    # ==================== Workers ====================
    
    def create_worker(
        self,
        worker_id: str,
        name: str,
        department: Optional[str] = None,
        shift: Optional[str] = None,
        is_active: bool = True
    ) -> Dict[str, Any]:
        """Create a new worker"""
        data = {
            "worker_id": worker_id,
            "name": name,
            "department": department,
            "shift": shift,
            "is_active": is_active
        }
        response = self.session.post(f"{self.base_url}/api/workers/", json=data)
        response.raise_for_status()
        return response.json()
    
    def get_all_workers(self, skip: int = 0, limit: int = 100, active_only: bool = True) -> List[Dict]:
        """Get all workers"""
        params = {"skip": skip, "limit": limit, "active_only": active_only}
        response = self.session.get(f"{self.base_url}/api/workers/", params=params)
        response.raise_for_status()
        return response.json()
    
    def get_worker(self, worker_id: int) -> Dict[str, Any]:
        """Get worker by database ID"""
        response = self.session.get(f"{self.base_url}/api/workers/{worker_id}")
        response.raise_for_status()
        return response.json()
    
    def get_worker_by_code(self, worker_code: str) -> Dict[str, Any]:
        """Get worker by worker code"""
        response = self.session.get(f"{self.base_url}/api/workers/code/{worker_code}")
        response.raise_for_status()
        return response.json()
    
    def update_worker(self, worker_id: int, **kwargs) -> Dict[str, Any]:
        """Update worker information"""
        response = self.session.put(f"{self.base_url}/api/workers/{worker_id}", json=kwargs)
        response.raise_for_status()
        return response.json()
    
    def delete_worker(self, worker_id: int) -> None:
        """Delete a worker"""
        response = self.session.delete(f"{self.base_url}/api/workers/{worker_id}")
        response.raise_for_status()
    
    # ==================== Incidents ====================
    
    def create_incident(
        self,
        incident_id: str,
        violation_type: str,
        worker_id: Optional[int] = None,
        zone_id: Optional[int] = None,
        description: Optional[str] = None,
        severity_score: float = 1.0
    ) -> Dict[str, Any]:
        """Create a new incident"""
        data = {
            "incident_id": incident_id,
            "violation_type": violation_type,
            "worker_id": worker_id,
            "zone_id": zone_id,
            "description": description,
            "severity_score": severity_score
        }
        response = self.session.post(f"{self.base_url}/api/incidents/", json=data)
        response.raise_for_status()
        return response.json()
    
    def get_all_incidents(
        self,
        skip: int = 0,
        limit: int = 100,
        status: Optional[str] = None,
        violation_type: Optional[str] = None,
        worker_id: Optional[int] = None
    ) -> List[Dict]:
        """Get all incidents with optional filters"""
        params = {
            "skip": skip,
            "limit": limit,
            "status": status,
            "violation_type": violation_type,
            "worker_id": worker_id
        }
        params = {k: v for k, v in params.items() if v is not None}
        response = self.session.get(f"{self.base_url}/api/incidents/", params=params)
        response.raise_for_status()
        return response.json()
    
    def get_incident(self, incident_id: int) -> Dict[str, Any]:
        """Get incident by database ID"""
        response = self.session.get(f"{self.base_url}/api/incidents/{incident_id}")
        response.raise_for_status()
        return response.json()
    
    def get_incident_by_code(self, incident_code: str) -> Dict[str, Any]:
        """Get incident by incident code"""
        response = self.session.get(f"{self.base_url}/api/incidents/code/{incident_code}")
        response.raise_for_status()
        return response.json()
    
    def update_incident(self, incident_id: int, **kwargs) -> Dict[str, Any]:
        """Update incident information"""
        response = self.session.put(f"{self.base_url}/api/incidents/{incident_id}", json=kwargs)
        response.raise_for_status()
        return response.json()
    
    def delete_incident(self, incident_id: int) -> None:
        """Delete an incident"""
        response = self.session.delete(f"{self.base_url}/api/incidents/{incident_id}")
        response.raise_for_status()
    
    # ==================== Safety Equipment ====================
    
    def create_equipment(
        self,
        equipment_type: str,
        equipment_id: str,
        is_required: bool = True,
        is_functional: bool = True,
        assigned_to: Optional[int] = None
    ) -> Dict[str, Any]:
        """Create new equipment"""
        data = {
            "equipment_type": equipment_type,
            "equipment_id": equipment_id,
            "is_required": is_required,
            "is_functional": is_functional,
            "assigned_to": assigned_to
        }
        response = self.session.post(f"{self.base_url}/api/safety-equipment/", json=data)
        response.raise_for_status()
        return response.json()
    
    def get_all_equipment(self, skip: int = 0, limit: int = 100, functional_only: bool = False) -> List[Dict]:
        """Get all equipment"""
        params = {"skip": skip, "limit": limit, "functional_only": functional_only}
        response = self.session.get(f"{self.base_url}/api/safety-equipment/", params=params)
        response.raise_for_status()
        return response.json()
    
    def get_equipment(self, equipment_id: int) -> Dict[str, Any]:
        """Get equipment by database ID"""
        response = self.session.get(f"{self.base_url}/api/safety-equipment/{equipment_id}")
        response.raise_for_status()
        return response.json()
    
    def get_equipment_by_code(self, equipment_code: str) -> Dict[str, Any]:
        """Get equipment by equipment code"""
        response = self.session.get(f"{self.base_url}/api/safety-equipment/code/{equipment_code}")
        response.raise_for_status()
        return response.json()
    
    def update_equipment(self, equipment_id: int, **kwargs) -> Dict[str, Any]:
        """Update equipment information"""
        response = self.session.put(f"{self.base_url}/api/safety-equipment/{equipment_id}", json=kwargs)
        response.raise_for_status()
        return response.json()
    
    def delete_equipment(self, equipment_id: int) -> None:
        """Delete equipment"""
        response = self.session.delete(f"{self.base_url}/api/safety-equipment/{equipment_id}")
        response.raise_for_status()
    
    # ==================== Restricted Zones ====================
    
    def create_zone(
        self,
        zone_name: str,
        zone_code: str,
        description: Optional[str] = None,
        coordinates: Optional[str] = None,
        risk_level: Optional[str] = "medium",
        is_active: bool = True
    ) -> Dict[str, Any]:
        """Create restricted zone"""
        data = {
            "zone_name": zone_name,
            "zone_code": zone_code,
            "description": description,
            "coordinates": coordinates,
            "risk_level": risk_level,
            "is_active": is_active
        }
        response = self.session.post(f"{self.base_url}/api/restricted-zones/", json=data)
        response.raise_for_status()
        return response.json()
    
    def get_all_zones(self, skip: int = 0, limit: int = 100, active_only: bool = True) -> List[Dict]:
        """Get all restricted zones"""
        params = {"skip": skip, "limit": limit, "active_only": active_only}
        response = self.session.get(f"{self.base_url}/api/restricted-zones/", params=params)
        response.raise_for_status()
        return response.json()
    
    def get_zone(self, zone_id: int) -> Dict[str, Any]:
        """Get zone by database ID"""
        response = self.session.get(f"{self.base_url}/api/restricted-zones/{zone_id}")
        response.raise_for_status()
        return response.json()
    
    def get_zone_by_code(self, zone_code: str) -> Dict[str, Any]:
        """Get zone by zone code"""
        response = self.session.get(f"{self.base_url}/api/restricted-zones/code/{zone_code}")
        response.raise_for_status()
        return response.json()
    
    def delete_zone(self, zone_id: int) -> None:
        """Delete a zone"""
        response = self.session.delete(f"{self.base_url}/api/restricted-zones/{zone_id}")
        response.raise_for_status()


# Example usage
if __name__ == "__main__":
    # Initialize client
    client = SafetyAPIClient()
    
    try:
        # Create a worker
        print("Creating worker...")
        worker = client.create_worker(
            worker_id="W001",
            name="John Doe",
            department="Manufacturing",
            shift="Morning"
        )
        print(f"Worker created: {worker}")
        
        # Get all workers
        print("\nGetting all workers...")
        workers = client.get_all_workers()
        print(f"Total workers: {len(workers)}")
        
        # Create an incident
        print("\nCreating incident...")
        incident = client.create_incident(
            incident_id="INC001",
            violation_type="no_helmet",
            worker_id=worker.get("id", 1),
            description="Worker without helmet in manufacturing area",
            severity_score=8.5
        )
        print(f"Incident created: {incident}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("Make sure the API is running at http://127.0.0.1:8000")
