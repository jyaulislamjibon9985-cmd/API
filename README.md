# Smart Industrial Safety Monitoring API

A comprehensive FastAPI-based REST API for monitoring workplace safety using AI and Computer Vision technology.

## Features

✅ **Complete CRUD Operations** for all safety entities  
✅ **Workers Management** - Track worker information and safety records  
✅ **Incident Management** - Log and track safety incidents  
✅ **Safety Equipment Management** - Monitor equipment status and functionality  
✅ **Restricted Zones** - Define and manage restricted work areas  
✅ **Equipment Detection Records** - Track equipment detection events  
✅ **Advanced Filtering** - Filter by status, violation type, worker, and more  
✅ **Swagger UI Documentation** - Interactive API documentation  
✅ **SQLite Database** - Local database (can be switched to PostgreSQL)  
✅ **RESTful Design** - Standards-compliant REST API  

## Quick Start

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
```bash
# If downloaded as ZIP, extract it
unzip industrial-safety-api.zip
cd "Industry Safety"
```

2. **Create a virtual environment (recommended)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**

   **Option A: Using the batch script (Windows)**
   ```bash
   run_server.bat
   ```

   **Option B: Using the shell script (macOS/Linux)**
   ```bash
   chmod +x run_server.sh
   ./run_server.sh
   ```

   **Option C: Manual command**
   ```bash
   python -m uvicorn main:app --reload
   ```

5. **Access the API**
   - API Root: http://127.0.0.1:8000
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

### Workers Management (`/api/workers`)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/workers/` | Create a new worker |
| GET | `/api/workers/` | List all workers |
| GET | `/api/workers/{worker_id}` | Get worker by ID |
| GET | `/api/workers/code/{worker_code}` | Get worker by code |
| PUT | `/api/workers/{worker_id}` | Update worker |
| DELETE | `/api/workers/{worker_id}` | Delete worker |

### Incidents Management (`/api/incidents`)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/incidents/` | Create incident |
| GET | `/api/incidents/` | List incidents |
| GET | `/api/incidents/{incident_id}` | Get incident by ID |
| GET | `/api/incidents/code/{incident_code}` | Get incident by code |
| PUT | `/api/incidents/{incident_id}` | Update incident |
| DELETE | `/api/incidents/{incident_id}` | Delete incident |

### Safety Equipment (`/api/safety-equipment`)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/safety-equipment/` | Create equipment |
| GET | `/api/safety-equipment/` | List equipment |
| GET | `/api/safety-equipment/{equipment_id}` | Get equipment by ID |
| GET | `/api/safety-equipment/code/{code}` | Get equipment by code |
| PUT | `/api/safety-equipment/{equipment_id}` | Update equipment |
| DELETE | `/api/safety-equipment/{equipment_id}` | Delete equipment |

### Restricted Zones (`/api/restricted-zones`)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/restricted-zones/` | Create zone |
| GET | `/api/restricted-zones/` | List zones |
| GET | `/api/restricted-zones/{zone_id}` | Get zone by ID |
| GET | `/api/restricted-zones/code/{code}` | Get zone by code |
| PUT | `/api/restricted-zones/{zone_id}` | Update zone |
| DELETE | `/api/restricted-zones/{zone_id}` | Delete zone |

### Equipment Records (`/api/equipment-records`)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/equipment-records/` | Create record |
| GET | `/api/equipment-records/` | List records |
| GET | `/api/equipment-records/{record_id}` | Get record by ID |
| GET | `/api/equipment-records/worker/{worker_id}` | Get records by worker |
| DELETE | `/api/equipment-records/{record_id}` | Delete record |

## Configuration

### Environment Variables
Create an `.env` file in the root directory:

```env
# Database Configuration
DATABASE_URL=sqlite:///./safety_monitoring.db
# For PostgreSQL: DATABASE_URL=postgresql://user:password@localhost/safety_monitoring_db

# Server Configuration
HOST=127.0.0.1
PORT=8000

# Security (for future implementation)
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Database
- **Default**: SQLite (automatic, no setup needed)
- **Alternative**: PostgreSQL (configure in `DATABASE_URL`)

## Project Structure

```
Industry Safety/
├── main.py                 # FastAPI application entry point
├── database.py             # Database configuration
├── models.py               # SQLAlchemy database models
├── schemas.py              # Pydantic request/response schemas
├── crud.py                 # CRUD operations for all entities
├── workers.py              # Worker API routes
├── incidents.py            # Incident API routes
├── safety_equipment.py      # Equipment API routes
├── restricted_zones.py      # Restricted zones routes
├── equipment_records.py     # Equipment records routes
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Project metadata
├── README.md                # This file
├── run_server.bat           # Windows batch script
├── run_server.sh            # Linux/macOS shell script
└── environments.env         # Environment variables template
```

## Usage Examples

### Using cURL

**Create a Worker**
```bash
curl -X POST "http://127.0.0.1:8000/api/workers/" \
  -H "Content-Type: application/json" \
  -d '{
    "worker_id": "W001",
    "name": "John Doe",
    "department": "Manufacturing",
    "shift": "Morning",
    "is_active": true
  }'
```

**Get All Workers**
```bash
curl "http://127.0.0.1:8000/api/workers/"
```

**Create an Incident**
```bash
curl -X POST "http://127.0.0.1:8000/api/incidents/" \
  -H "Content-Type: application/json" \
  -d '{
    "incident_id": "INC001",
    "violation_type": "no_helmet",
    "worker_id": 1,
    "description": "Worker without helmet in manufacturing area",
    "severity_score": 8.5
  }'
```

### Using Python Requests

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Create a worker
response = requests.post(
    f"{BASE_URL}/api/workers/",
    json={
        "worker_id": "W001",
        "name": "John Doe",
        "department": "Manufacturing",
        "shift": "Morning"
    }
)
print(response.json())

# Get all workers
response = requests.get(f"{BASE_URL}/api/workers/")
print(response.json())
```

## Docker Support

### Build Docker Image
```bash
docker build -t industrial-safety-api:latest .
```

### Run Container
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=sqlite:///./safety_monitoring.db \
  industrial-safety-api:latest
```

## Deployment

### Heroku
```bash
heroku create your-app-name
git push heroku main
heroku open
```

### DigitalOcean
See `deployment/digitalocean-guide.md`

### AWS
See `deployment/aws-guide.md`

## Testing

Run the test suite:
```bash
pytest
pytest -v  # Verbose
pytest --cov=  # With coverage
```

## Performance Optimization

- **Pagination**: Use `skip` and `limit` parameters to handle large datasets
- **Filtering**: Filter by status, violation type, etc., on the server side
- **Indexing**: Database queries are optimized with proper indexes
- **Caching**: Consider implementing Redis for frequently accessed data

## Security Considerations

⚠️ **Before Production Deployment**:
1. Change `SECRET_KEY` in environment variables
2. Set `ALGORITHM` to a secure value
3. Configure CORS properly for your domain
4. Use HTTPS/TLS for all connections
5. Implement authentication (JWT tokens)
6. Set up rate limiting
7. Add input validation
8. Keep dependencies updated

## Troubleshooting

### Port Already in Use
```bash
# Find and kill process on port 8000
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :8000
kill -9 <PID>
```

### Database Errors
```bash
# Reset database
rm safety_monitoring.db
python -m uvicorn main:app --reload
```

### Module Not Found
```bash
# Reinstall dependencies
pip install --upgrade --force-reinstall -r requirements.txt
```

## API Documentation

Detailed API documentation is available at:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **OpenAPI JSON**: http://127.0.0.1:8000/openapi.json

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Email: support@example.com
- Documentation: http://127.0.0.1:8000/docs

## Version History

### v1.0.0 (2026-07-08)
- Initial release
- Complete CRUD operations for all entities
- Swagger UI documentation
- SQLite database support
- RESTful API design

## Roadmap

- [ ] User authentication and authorization
- [ ] Advanced analytics and reporting
- [ ] Real-time notifications
- [ ] Mobile app integration
- [ ] AI-powered incident prediction
- [ ] Integration with surveillance systems
- [ ] Multi-language support
- [ ] Performance dashboards

---

**Built with FastAPI** ⚡ | **Powered by SQLAlchemy** 🗄️ | **Documented with Swagger** 📖
