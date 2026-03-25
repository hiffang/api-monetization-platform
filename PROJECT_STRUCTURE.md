# Project Structure

```
api-monetization-platform/
│
├── 📄 README.md                 # Main project documentation
├── 📄 DEVELOPMENT.md            # Development setup guide
├── 📄 CONTRIBUTING.md           # Contribution guidelines
├── 📄 docker-compose.yml        # Container orchestration
│
├── 📁 backend-api/              # FastAPI backend service
│   ├── 📁 app/                  # Application package
│   │   ├── 📄 __init__.py       # App factory
│   │   ├── 📄 main.py           # FastAPI setup and routes
│   │   │
│   │   ├── 📁 routes/           # API endpoints
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 health.py     # Health check endpoints
│   │   │   └── 📄 api_v1.py     # v1 API routes
│   │   │
│   │   ├── 📁 models/           # Pydantic data models
│   │   │   ├── 📄 __init__.py
│   │   │   └── 📄 schemas.py    # (Add request/response models)
│   │   │
│   │   ├── 📁 services/         # Business logic layer
│   │   │   ├── 📄 __init__.py
│   │   │   └── 📄 (services)    # Domain-specific services
│   │   │
│   │   ├── 📁 middleware/       # Custom middleware
│   │   │   ├── 📄 __init__.py
│   │   │   └── 📄 logging.py    # Request logging middleware
│   │   │
│   │   └── 📁 utils/            # Utility functions
│   │       ├── 📄 __init__.py
│   │       └── 📄 (helpers)     # Helper utilities
│   │
│   ├── 📄 config.py             # Application configuration
│   ├── 📄 main.py               # Application entry point
│   ├── 📄 requirements.txt       # Python dependencies
│   ├── 📄 tests.py              # Test suite
│   ├── 📄 Dockerfile            # Container image definition
│   ├── 📄 .env.example          # Environment variables template
│   ├── 📄 .gitignore            # Git ignore rules
│   └── 📄 README.md             # Backend API documentation
│
├── 📁 billing-service/          # Payment processing service
│   ├── 📁 app/
│   │   ├── 📁 routes/
│   │   ├── 📁 models/
│   │   ├── 📁 services/
│   │   └── 📁 middleware/
│   ├── 📄 config.py
│   ├── 📄 main.py
│   ├── 📄 requirements.txt
│   ├── 📄 Dockerfile
│   ├── 📄 .env.example
│   └── 📄 README.md
│
├── 📁 apis/                     # API definitions & specifications
│   └── 📄 (OpenAPI specs)       # (To be added)
│
└── 📁 docs/                     # Project documentation
    ├── 📄 API.md                # API specification (To be added)
    ├── 📄 ARCHITECTURE.md       # Architecture decisions (To be added)
    └── 📄 DEPLOYMENT.md         # Deployment guide (To be added)
```

## Key Files Overview

### Configuration & Setup
- `config.py` - Centralized settings management
- `requirements.txt` - Python package dependencies
- `.env.example` - Environment variables template
- `.gitignore` - Git ignore rules

### Application Code
- `app/main.py` - FastAPI application setup
- `app/routes/` - API endpoints organized by feature
- `app/models/` - Pydantic schemas and data models
- `app/services/` - Business logic layer
- `app/middleware/` - Custom middleware (logging, auth, etc.)
- `app/utils/` - Reusable utility functions

### Testing & Documentation
- `tests.py` - Unit and integration tests
- `README.md` - Service documentation
- `Dockerfile` - Container image configuration

### DevOps
- `docker-compose.yml` - Multi-container orchestration
- `Dockerfile` - Individual service containerization

## Development Workflow

1. **Add Routes** → `app/routes/`
2. **Define Models** → `app/models/`
3. **Implement Logic** → `app/services/`
4. **Add Middleware** → `app/middleware/`
5. **Write Tests** → `tests.py`
6. **Document** → Update README.md

## Running Services

### Local Development
```bash
cd backend-api
python main.py
```

### Docker Containers
```bash
docker-compose up
```

### Services Started
- Backend API: http://localhost:8000
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- WSO2 API Manager: https://localhost:9443

## Next Steps

1. ✅ Backend API structure implemented
2. ⏳ Implement billing-service (follow same pattern)
3. ⏳ Add database models and migrations
4. ⏳ Add service-to-service communication
5. ⏳ Setup CI/CD pipeline
6. ⏳ Add monitoring and alerting

See [DEVELOPMENT.md](../DEVELOPMENT.md) for detailed setup instructions.
