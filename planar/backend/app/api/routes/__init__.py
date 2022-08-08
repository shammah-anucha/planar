from fastapi import APIRouter
from app.api.routes.services import router as services_router

router = APIRouter()

router.include_router(services_router, prefix="/services", tags=["services"])
