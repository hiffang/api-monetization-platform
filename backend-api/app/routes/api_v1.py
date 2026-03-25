"""API v1 routes"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def hello() -> dict:
    """Hello endpoint"""
    return {
        "message": "Hello from API Monetization Platform Backend",
        "status": "success",
        "version": "1.0"
    }
