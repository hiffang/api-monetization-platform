"""Health check endpoints"""

from datetime import datetime
from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "backend-api"
    }


@router.get("/ready")
async def readiness_check() -> dict:
    """Readiness check endpoint"""
    return {
        "status": "ready",
        "timestamp": datetime.utcnow().isoformat()
    }
