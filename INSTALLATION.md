# Installation and Setup Guide

## Quick Start (< 2 minutes)

### Windows
1. Extract the ZIP file
2. Double-click `run_server.bat`
3. Open http://127.0.0.1:8000/docs

### macOS/Linux
1. Extract the ZIP file
2. Run: `chmod +x run_server.sh && ./run_server.sh`
3. Open http://127.0.0.1:8000/docs

---

## Detailed Installation

### Step 1: System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python**: 3.9 or higher
- **RAM**: Minimum 512MB, Recommended 1GB+
- **Disk Space**: ~500MB

### Step 2: Install Python

#### Windows
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. ✅ **Important**: Check "Add Python to PATH"
4. Click Install

#### macOS
```bash
# Using Homebrew
brew install python3@3.11
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3.11 python3-pip
```

### Step 3: Extract the Application
- Extract `industrial-safety-api.zip` to your desired location
- Note the extracted folder path

### Step 4: Install Dependencies

#### Option A: Automatic (Easiest)
- **Windows**: Double-click `run_server.bat`
- **macOS/Linux**: Run `./run_server.sh`

#### Option B: Manual
```bash
# Navigate to project directory
cd "path/to/Industry Safety"

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 5: Run the Application

#### Option A: Using Startup Scripts (Recommended)
```bash
# Windows
run_server.bat

# macOS/Linux
./run_server.sh
```

#### Option B: Manual Command
```bash
python -m uvicorn main:app --reload
```

### Step 6: Access the Application
- **API Root**: http://127.0.0.1:8000
- **API Documentation**: http://127.0.0.1:8000/docs
- **Alternative Docs**: http://127.0.0.1:8000/redoc

---

## Using Docker (Optional)

### Prerequisites
- Install Docker Desktop from https://www.docker.com/products/docker-desktop

### Installation
```bash
# Build the image
docker build -t industrial-safety-api:latest .

# Run the container
docker run -p 8000:8000 industrial-safety-api:latest

# Access at http://127.0.0.1:8000/docs
```

### Using Docker Compose (Easier)
```bash
# Start the application
docker-compose up

# Stop the application
docker-compose down
```

---

## Package Installation Methods

### Method 1: pip (If you publish to PyPI)
```bash
pip install industrial-safety-api
```

### Method 2: From Source
```bash
# Extract ZIP
cd industrial-safety-api

# Create virtual environment
python -m venv venv

# Activate and install
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install .
```

### Method 3: Development Installation
```bash
pip install -e ".[dev]"
```

---

## Troubleshooting

### "Python is not installed or not in PATH"
**Solution**:
1. Download Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart your computer
4. Try again

### "ModuleNotFoundError: No module named 'fastapi'"
**Solution**:
```bash
# Make sure you're in the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Then install dependencies
pip install -r requirements.txt
```

### "Address already in use" (Port 8000 in use)
**Solution**:
```bash
# Kill process using port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :8000
kill -9 <PID>
```

### Database Error
**Solution**:
```bash
# Delete the old database and restart
rm safety_monitoring.db  # macOS/Linux
del safety_monitoring.db # Windows

# Run the application again
```

---

## Upgrading

### Upgrade Dependencies
```bash
# Activate virtual environment first
pip install --upgrade -r requirements.txt
```

### Upgrade the Application
1. Download the latest version
2. Backup your current installation
3. Copy new files (except `safety_monitoring.db`)
4. Run the startup script

---

## Configuration

### Environment Variables
Create a `.env` file in the project directory:

```env
# Database
DATABASE_URL=sqlite:///./safety_monitoring.db
# For PostgreSQL: postgresql://user:password@localhost/safety_monitoring_db

# Server
HOST=127.0.0.1
PORT=8000

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Database Configuration

#### SQLite (Default)
No configuration needed. Database is created automatically.

#### PostgreSQL
1. Install PostgreSQL from https://www.postgresql.org/download/
2. Create database: `createdb safety_monitoring_db`
3. Set `DATABASE_URL` in `.env`

---

## Performance Tips

1. **Use Virtual Environment**: Keeps dependencies isolated
2. **Pagination**: Use `skip` and `limit` in API calls
3. **Filtering**: Use server-side filtering
4. **Caching**: Consider Redis for frequently accessed data
5. **Database**: Use PostgreSQL for production
6. **Monitoring**: Monitor server logs for issues

---

## Production Deployment

### Before Deploying

⚠️ Security checklist:
- [ ] Change `SECRET_KEY` in `.env`
- [ ] Set `DEBUG = False`
- [ ] Use HTTPS/TLS
- [ ] Configure CORS properly
- [ ] Set strong database password
- [ ] Enable authentication
- [ ] Set rate limiting
- [ ] Update dependencies

### Deployment Options

1. **Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

2. **DigitalOcean**
   - Use DigitalOcean App Platform
   - Connect GitHub repository
   - Deploy on push

3. **AWS**
   - Use Elastic Beanstalk
   - Or deploy on EC2 with Docker

4. **Docker Hub**
   ```bash
   docker build -t your-username/industrial-safety-api .
   docker push your-username/industrial-safety-api
   ```

---

## Getting Help

- 📖 **Documentation**: http://localhost:8000/docs
- 🐛 **Issues**: Check troubleshooting section
- 💬 **Community**: Refer to GitHub discussions
- 📧 **Support**: support@example.com

---

## What's Next?

- [ ] Test API endpoints in Swagger UI
- [ ] Read through the README.md
- [ ] Set up environment variables
- [ ] Configure database if needed
- [ ] Integrate with your systems
- [ ] Deploy to production

Happy coding! 🚀
