"""FastAPI application factory and initialization"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import health, api_v1
from app.middleware.logging import LoggingMiddleware
from config import settings

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle startup and shutdown events"""
    logger.info("Starting up Backend API")
    yield
    logger.info("Shutting down Backend API")


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    
    app = FastAPI(
        title="API Monetization Platform - Backend API",
        description="Backend API for managing API monetization",
        version="0.1.0",
        lifespan=lifespan,
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Add logging middleware
    app.add_middleware(LoggingMiddleware)
    
    # Include routers
    app.include_router(health.router, tags=["health"])
    app.include_router(api_v1.router, prefix="/api/v1", tags=["api"])
    
    logger.info(f"API running in {settings.ENVIRONMENT} mode")
    
    return app


app = create_app()
