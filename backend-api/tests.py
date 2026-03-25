"""Example tests for the backend API"""

import pytest
from fastapi.testclient import TestClient
from app.main import create_app


@pytest.fixture
def client():
    """Create a test client"""
    app = create_app()
    return TestClient(app)


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_readiness_check(client):
    """Test readiness check endpoint"""
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_hello_endpoint(client):
    """Test hello API endpoint"""
    response = client.get("/api/v1/hello")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
