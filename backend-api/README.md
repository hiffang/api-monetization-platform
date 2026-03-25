# Backend API

FastAPI-based backend service for the API Monetization Platform.

## 📋 Overview

This service handles:
- API health checks and monitoring
- Core business logic
- Database interactions
- External service integrations (Stripe, etc.)
- Request/response logging and middleware

## 🏗️ Project Structure

```
backend-api/
├── app/
│   ├── __init__.py          # App factory
│   ├── main.py              # FastAPI setup
│   ├── routes/              # API endpoints
│   │   ├── health.py        # Health check endpoints
│   │   └── api_v1.py        # v1 API routes
│   ├── models/              # Pydantic models
│   ├── services/            # Business logic
│   ├── middleware/          # Custom middleware
│   │   └── logging.py       # Request logging
│   └── utils/               # Utility functions
├── config.py                # Configuration management
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── Dockerfile              # Container configuration
├── .env.example            # Environment variables template
└── .gitignore              # Git ignore rules
```

## ✨ Features

- **Modular Architecture**: Organized by concern (routes, services, models)
- **Middleware Support**: Logging, CORS, error handling
- **Configuration Management**: Environment-based settings
- **Health Checks**: Readiness and liveness probes
- **API Versioning**: Support for multiple API versions (v1, v2, etc.)
- **Comprehensive Logging**: Request/response logging with timing

## 🚀 Getting Started

### 1. Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy the example and customize
cp .env.example .env

# Edit .env with your settings
```

### 4. Run Development Server

```bash
python main.py
```

Server will start at `http://localhost:8000`

### 5. Access API Documentation

- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 📚 Available Endpoints

### Health Checks
- `GET /health` - Service health status
- `GET /ready` - Service readiness status

### API v1
- `GET /api/v1/hello` - Sample endpoint

## 🧪 Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov

# Specific test file
pytest tests/test_health.py -v
```

## 🔍 Configuration

All configuration is managed through `config.py` and environment variables:

```python
# Example from .env
APP_NAME=API Monetization Platform Backend
ENVIRONMENT=development
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/api_monetization
SECRET_KEY=your-secret-key
```

## 🔌 Adding New Routes

1. Create a new file in `app/routes/`
2. Define your router:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
async def get_items():
    return {"items": []}
```

3. Include in `app/main.py`:

```python
from app.routes import my_routes
app.include_router(my_routes.router, prefix="/api/v1")
```

## 🛠️ Development Tools

### Code Formatting
```bash
black .
```

### Linting
```bash
flake8 .
```

### Import Sorting
```bash
isort .
```

## 🐳 Docker

### Build Image
```bash
docker build -t api-monetization-backend .
```

### Run Container
```bash
docker run -p 8000:8000 --env-file .env api-monetization-backend
```

### Using Docker Compose
```bash
docker-compose up backend-api
```

## 📊 Logging

The application uses Python's standard logging module with:
- Formatted timestamps
- Log levels (DEBUG, INFO, WARNING, ERROR)
- Request/response tracking

View logs:
```bash
tail -f logs/app.log
```

## 🔐 Security Considerations

- Keep `.env` and `SECRET_KEY` secure
- Update `CORS_ORIGINS` for production
- Use environment variables for sensitive data
- Validate all inputs
- Use HTTPS in production

## 📦 Dependencies

See [requirements.txt](requirements.txt) for detailed version information:

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **pydantic**: Data validation
- **sqlalchemy**: ORM
- **psycopg2**: PostgreSQL adapter
- **python-dotenv**: Environment management

## 🚨 Troubleshooting

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

### Database Connection Issues
- Verify `DATABASE_URL` in `.env`
- Ensure PostgreSQL is running
- Check connection permissions

### Port Already in Use
```bash
# Change PORT in .env or
python main.py --port 8001
```

## 📝 Next Steps

- [ ] Add database models in `app/models/`
- [ ] Implement services in `app/services/`
- [ ] Add authentication/authorization
- [ ] Create comprehensive test suite
- [ ] Setup CI/CD pipeline

## 📖 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
