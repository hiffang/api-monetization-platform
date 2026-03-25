# API Monetization Platform

A comprehensive platform for managing, monetizing, and monitoring APIs with built-in billing and usage tracking capabilities.

## 📁 Project Structure

```
api-monetization-platform/
├── backend-api/          # FastAPI backend service
├── billing-service/      # Billing and payment processing service
├── apis/                 # API definitions and specifications
├── docs/                 # Project documentation
├── docker-compose.yml    # Container orchestration
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)
- PostgreSQL 15+ (or use docker)

### Running with Docker Compose

```bash
docker-compose up -d
```

This will start:
- **Backend API**: http://localhost:8000
- **PostgreSQL Database**: localhost:5432
- **Redis Cache**: localhost:6379
- **WSO2 API Manager**: https://localhost:9443

### Local Development

1. Navigate to the backend-api directory:
```bash
cd backend-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file from `.env.example` and configure settings

5. Run the development server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## 📚 Documentation

- [Backend API Documentation](backend-api/README.md)
- [API Specifications](docs/API.md)
- [Architecture Guide](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🏗️ Key Features

- **API Management**: Register, manage, and version APIs
- **Usage Tracking**: Monitor API usage and analytics
- **Billing Integration**: Automated billing with Stripe/PayPal
- **Rate Limiting**: Built-in rate limiting and throttling
- **Authentication**: JWT-based API key management
- **Monitoring**: Real-time metrics and logging

## 🔧 Development

### Running Tests
```bash
cd backend-api
pytest
```

### Code Quality
```bash
black .              # Format code
flake8 .             # Lint code
isort .              # Sort imports
```

### API Documentation
Once running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔐 Security

- Environment variables for sensitive data (see `.env.example`)
- CORS configuration
- Rate limiting on API endpoints
- JWT token authentication

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please follow the development guidelines in [CONTRIBUTING.md](CONTRIBUTING.md)
