# ⚡ Quick Start Guide

Get the Industrial Safety Monitoring API running in **less than 2 minutes**.

## For Windows Users

### Step 1: Extract Files
- Extract `industrial-safety-api.zip` to your preferred location

### Step 2: Double-Click to Start
- Open the extracted folder
- **Double-click `run_server.bat`**
- A command prompt will open automatically

### Step 3: Wait for Startup
- Wait for the message: `Application startup complete`
- You should see: `Uvicorn running on http://127.0.0.1:8000`

### Step 4: Open in Browser
- Open: **http://127.0.0.1:8000/docs**
- You'll see the interactive API documentation

✅ **Done!** The API is running.

---

## For macOS/Linux Users

### Step 1: Extract Files
```bash
unzip industrial-safety-api.zip
cd "Industry Safety"
```

### Step 2: Make Startup Script Executable
```bash
chmod +x run_server.sh
```

### Step 3: Run the Application
```bash
./run_server.sh
```

### Step 4: Open in Browser
- Open: **http://127.0.0.1:8000/docs**
- You'll see the interactive API documentation

✅ **Done!** The API is running.

---

## Testing the API

### Via Web Browser (Easiest)
1. Go to http://127.0.0.1:8000/docs
2. Click on any endpoint (e.g., `POST /api/workers/`)
3. Click "Try it out"
4. Fill in the form
5. Click "Execute"

### Example: Create a Worker

In Swagger UI:
1. Find `POST /api/workers/` under "workers" section
2. Click "Try it out"
3. In the request body, paste:
```json
{
  "worker_id": "W001",
  "name": "John Doe",
  "department": "Manufacturing",
  "shift": "Morning",
  "is_active": true
}
```
4. Click "Execute"
5. You'll see the response with status 201 ✅

### Via cURL

```bash
curl -X POST "http://127.0.0.1:8000/api/workers/" \
  -H "Content-Type: application/json" \
  -d '{
    "worker_id": "W001",
    "name": "John Doe",
    "department": "Manufacturing",
    "shift": "Morning"
  }'
```

### Via Python

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/api/workers/",
    json={
        "worker_id": "W001",
        "name": "John Doe",
        "department": "Manufacturing",
        "shift": "Morning"
    }
)

print(response.json())
```

---

## Common Endpoints to Try

### Workers
- **Create**: `POST /api/workers/`
- **List**: `GET /api/workers/`
- **Get One**: `GET /api/workers/{worker_id}`

### Incidents
- **Create**: `POST /api/incidents/`
- **List**: `GET /api/incidents/`
- **Filter**: `GET /api/incidents/?status=pending`

### Equipment
- **Create**: `POST /api/safety-equipment/`
- **List**: `GET /api/safety-equipment/`
- **Functional Only**: `GET /api/safety-equipment/?functional_only=true`

### Zones
- **Create**: `POST /api/restricted-zones/`
- **List**: `GET /api/restricted-zones/`

---

## Stopping the Server

- **Windows**: Press `Ctrl+C` in the command prompt
- **macOS/Linux**: Press `Ctrl+C` in the terminal

---

## API Endpoints Reference

### Format
- **GET**: Read data
- **POST**: Create data  
- **PUT**: Update data
- **DELETE**: Remove data

### Status Codes
- **200**: OK (success)
- **201**: Created (new resource)
- **204**: No Content (deleted)
- **400**: Bad Request
- **404**: Not Found
- **409**: Conflict (duplicate)
- **500**: Server Error

---

## Documentation

For more details:
- 📖 **Full Documentation**: [README.md](README.md)
- 🚀 **Installation Guide**: [INSTALLATION.md](INSTALLATION.md)
- 🌐 **Deployment Guide**: [DEPLOYMENT.md](DEPLOYMENT.md)
- 🐍 **Python Client**: [client.py](client.py)

---

## Troubleshooting

### "Port already in use"
```bash
# Kill the process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :8000
kill -9 <PID>
```

### "ModuleNotFoundError"
- The startup script should install dependencies automatically
- If not, run: `pip install -r requirements.txt`

### "Database error"
- Delete `safety_monitoring.db` file
- Run the startup script again
- Database will be recreated automatically

### "Python not found"
- Install Python 3.9+ from https://www.python.org/downloads/
- On Windows, check "Add Python to PATH" during installation

---

## Next Steps

1. ✅ **API Running**: You have the API up and running
2. 📚 **Explore Endpoints**: Try creating workers, incidents, etc.
3. 🔧 **Configure Database**: Switch to PostgreSQL if needed
4. 🚀 **Deploy**: Deploy to cloud (Heroku, AWS, etc.)
5. 🔐 **Secure**: Change SECRET_KEY before production

---

## Need Help?

- Check the **[README.md](README.md)** for detailed documentation
- See **[INSTALLATION.md](INSTALLATION.md)** for installation issues
- Check **[DEPLOYMENT.md](DEPLOYMENT.md)** for deployment options
- Review API docs at: http://127.0.0.1:8000/docs

---

**Enjoy using the Industrial Safety Monitoring API!** 🎉

For issues or questions, check the troubleshooting section or refer to the full documentation.
