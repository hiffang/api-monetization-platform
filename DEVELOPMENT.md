# Development Setup Guide

This guide walks you through setting up the API Monetization Platform for development.

## Prerequisites

- **Python**: 3.11 or higher
- **Git**: Latest version
- **Docker & Docker Compose** (optional, for containerized development)
- **PostgreSQL**: 15+ (or use Docker)

## Step 1: Clone and Navigate

```bash
cd api-monetization-platform
```

## Step 2: Backend API Setup

### Create Virtual Environment

```bash
cd backend-api

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

```bash
# Copy example configuration
cp .env.example .env

# Edit .env with your settings (optional for development)
```

### Run Development Server

```bash
python main.py
```

The API will be available at: **http://localhost:8000**

## Step 3: Test the API

### Using Browser
Open: http://localhost:8000/docs (Interactive Swagger UI)

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Hello endpoint
curl http://localhost:8000/api/v1/hello
```

### Using Python

```python
import requests

response = requests.get("http://localhost:8000/health")
print(response.json())
```

### Run Automated Tests

```bash
pytest tests.py -v
```

## Step 4: Full Stack with Docker

From the project root:

```bash
docker-compose up -d
```

This starts:
- Backend API: http://localhost:8000
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- WSO2 API Manager: https://localhost:9443

Check status:
```bash
docker-compose ps
```

View logs:
```bash
docker-compose logs -f backend-api
```

Stop services:
```bash
docker-compose down
```

## Step 5: Database Setup (Optional)

### With Docker

```bash
# PostgreSQL is automatically started with docker-compose
psql -h localhost -U api_user -d api_monetization
```

### Manual PostgreSQL

```bash
# Create database
createdb api_monetization

# Connect
psql api_monetization
```

## Step 6: Code Quality

### Format Code

```bash
black backend-api/
```

### Lint Code

```bash
flake8 backend-api/
```

### Sort Imports

```bash
isort backend-api/
```

### Run All Quality Checks

```bash
cd backend-api
black . && flake8 . && isort .
```

## Common Development Tasks

### Adding a New Endpoint

1. Create file in `backend-api/app/routes/`
2. Define FastAPI router
3. Include router in `backend-api/app/main.py`
4. Test with: `http://localhost:8000/docs`

### Adding Dependencies

1. Update `backend-api/requirements.txt`
2. Run: `pip install -r requirements.txt`

### Environment Variables

Edit `backend-api/.env`:

```env
DEBUG=True
LOG_LEVEL=INFO
DATABASE_URL=postgresql://localhost/api_monetization
```

## Troubleshooting

### Virtual Environment Issues

```bash
# Fully recreate venv
rm -rf venv
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

### Port 8000 Already in Use

```bash
# Change port in .env
PORT=8001

# Or find and kill process
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows
```

### Database Connection Issues

```bash
# Verify PostgreSQL is running
psql --version

# Check connection string in .env
DATABASE_URL=postgresql://user:password@localhost:5432/api_monetization
```

### Docker Issues

```bash
# Remove all containers and restart
docker-compose down -v
docker-compose up -d

# View logs
docker-compose logs backend-api

# Rebuild images
docker-compose build --no-cache
```

## Next Steps

1. **Read Documentation**: See [backend-api/README.md](backend-api/README.md)
2. **Explore API**: Visit http://localhost:8000/docs
3. **Run Tests**: `pytest backend-api/tests.py -v`
4. **Add Features**: Create new endpoints following the existing patterns

## Useful Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## Getting Help

- Check logs: `docker-compose logs backend-api`
- Read error messages carefully
- Verify all prerequisites are installed
- Check .env configuration
