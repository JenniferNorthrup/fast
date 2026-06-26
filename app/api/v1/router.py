from fastapi import APIRouter
from app.api.v1.routes.items import items_router
from app.api.v1.routes.employees import employees_router
internal_router = APIRouter()

internal_router.include_router(items_router)
internal_router.include_router(employees_router)
