# Deployment Guide

## Deployment Options

Choose a deployment platform based on your needs:

- **Local**: Development and testing
- **Docker**: Containerized deployment (any cloud)
- **Heroku**: Simple cloud deployment (5-10 min)
- **DigitalOcean**: Virtual private server
- **AWS**: Scalable enterprise solution
- **Azure**: Microsoft cloud platform

---

## 1. Local Deployment

### Windows
```batch
run_server.bat
```

### macOS/Linux
```bash
chmod +x run_server.sh
./run_server.sh
```

**Access**: http://127.0.0.1:8000/docs

---

## 2. Docker Deployment

### Build and Run

```bash
# Build image
docker build -t industrial-safety-api:latest .

# Run container
docker run -p 8000:8000 \
  -e DATABASE_URL=sqlite:///./data/safety_monitoring.db \
  industrial-safety-api:latest

# Access
# http://localhost:8000/docs
```

### Using Docker Compose

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f api
```

**With PostgreSQL**:
```bash
# Edit docker-compose.yml to uncomment PostgreSQL service
docker-compose up -d

# API will use PostgreSQL automatically
```

---

## 3. Heroku Deployment

### Prerequisites
- Heroku account (free or paid)
- Heroku CLI installed

### Steps

```bash
# 1. Create Heroku app
heroku create your-app-name

# 2. Add PostgreSQL (optional)
heroku addons:create heroku-postgresql:hobby-dev

# 3. Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set ALGORITHM="HS256"

# 4. Deploy
git push heroku main

# 5. Open app
heroku open

# 6. View logs
heroku logs --tail
```

**Procfile**:
```
web: uvicorn main:app --host=0.0.0.0 --port=${PORT}
```

---

## 4. DigitalOcean Deployment

### Using App Platform (Easiest)

1. Connect GitHub repository to DigitalOcean
2. Create new app from repository
3. Select the repo and branch
4. Configure:
   - **Build command**: `pip install -r requirements.txt`
   - **Run command**: `uvicorn main:app --host 0.0.0.0 --port 8080`
   - **HTTP port**: 8080
5. Add environment variables
6. Deploy

### Using Droplet (Virtual Machine)

```bash
# SSH into droplet
ssh root@your_droplet_ip

# Update system
apt-get update && apt-get upgrade -y

# Install Python and dependencies
apt-get install -y python3.11 python3-pip supervisor nginx

# Clone or upload your application
git clone your-repo-url
cd industrial-safety-api

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Set up Supervisor for auto-restart
# Create /etc/supervisor/conf.d/api.conf

# Set up Nginx reverse proxy
# Configure /etc/nginx/sites-available/default

# Restart services
systemctl restart supervisor nginx
```

**Supervisor config** (`/etc/supervisor/conf.d/api.conf`):
```ini
[program:industrial-safety-api]
directory=/home/appuser/industrial-safety-api
command=/home/appuser/industrial-safety-api/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
autostart=true
autorestart=true
stderr_logfile=/var/log/api.err.log
stdout_logfile=/var/log/api.out.log
```

---

## 5. AWS Deployment

### Using Elastic Beanstalk (Easiest)

```bash
# 1. Install EB CLI
pip install awsebcli

# 2. Initialize EB app
eb init -p python-3.11 industrial-safety-api

# 3. Create environment
eb create production

# 4. Set environment variables
eb setenv DATABASE_URL=your-rds-url SECRET_KEY=your-key

# 5. Deploy
eb deploy

# 6. Open in browser
eb open
```

### Using EC2

1. Launch EC2 instance (Ubuntu 22.04)
2. SSH into instance
3. Install Python 3.11+
4. Clone repository
5. Set up as described in DigitalOcean section
6. Configure security groups for port 80/443

---

## 6. Azure Deployment

### Using App Service

1. Create App Service
2. Connect GitHub repository
3. Configure:
   - Python runtime: 3.11
   - Startup command: `python -m uvicorn main:app --host 0.0.0.0`
4. Add application settings (environment variables)
5. Deploy

---

## 7. Railway.app Deployment

```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Initialize project
railway init

# 4. Add PostgreSQL (optional)
railway add

# 5. Deploy
railway up

# 6. View URL
railway open
```

---

## Production Checklist

### Security

- [ ] Change `SECRET_KEY` to strong random value
- [ ] Set `DEBUG=False`
- [ ] Configure HTTPS/TLS certificate
- [ ] Set up CORS for specific domains
- [ ] Enable authentication/authorization
- [ ] Implement rate limiting
- [ ] Set up Web Application Firewall (WAF)
- [ ] Enable logging and monitoring
- [ ] Regular security updates

### Database

- [ ] Use PostgreSQL (not SQLite in production)
- [ ] Set strong database password
- [ ] Enable backup and recovery
- [ ] Configure database firewall
- [ ] Monitor database performance
- [ ] Set up connection pooling

### Infrastructure

- [ ] Use load balancer
- [ ] Set up auto-scaling
- [ ] Configure CDN
- [ ] Enable caching
- [ ] Set up monitoring and alerts
- [ ] Configure logging
- [ ] Enable backups

### Monitoring

- [ ] Set up uptime monitoring
- [ ] Configure error tracking (Sentry, etc.)
- [ ] Monitor resource usage
- [ ] Set up performance monitoring
- [ ] Track API usage metrics

---

## Performance Optimization

### Database
```python
# Use connection pooling
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_MAX_OVERFLOW = 40
```

### Caching
```python
# Add Redis for caching
pip install redis
```

### API Response
```python
# Use pagination
?skip=0&limit=50

# Use compression
pip install fastapi-gzip
```

---

## Scaling Considerations

### Horizontal Scaling
- Load balance across multiple instances
- Use database like PostgreSQL
- Implement caching layer (Redis)
- Use CDN for static content

### Vertical Scaling
- Increase server resources (CPU, RAM)
- Optimize database queries
- Enable query caching
- Use connection pooling

---

## Troubleshooting

### Application won't start
```bash
# Check logs
docker logs container_id
heroku logs --tail
journalctl -u your-service -n 50
```

### Database connection issues
- Verify connection string
- Check database server is running
- Verify credentials
- Check firewall rules

### Performance issues
- Monitor CPU/memory usage
- Check database query performance
- Enable caching
- Optimize API endpoints

### SSL Certificate issues
- Renew certificate before expiration
- Verify certificate path
- Check certificate permissions

---

## Monitoring Tools

- **Uptime**: Uptime Robot, StatusPage
- **Errors**: Sentry, Rollbar
- **Performance**: New Relic, DataDog
- **Logs**: ELK Stack, Splunk, CloudWatch
- **APM**: New Relic, DataDog, Elastic APM

---

## Backup Strategy

### Daily Backups
```bash
# Automated daily backup
0 2 * * * pg_dump safety_monitoring_db | gzip > /backups/db_$(date +\%Y\%m\%d).sql.gz
```

### Cloud Backups
- AWS S3
- Google Cloud Storage
- Azure Blob Storage

### Recovery Testing
- Test recovery monthly
- Document recovery procedure

---

## Support

For deployment issues:
1. Check logs
2. Verify environment variables
3. Test locally first
4. Check documentation
5. Contact support
