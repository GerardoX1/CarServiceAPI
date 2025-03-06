from fastapi import APIRouter, FastAPI

from .endpoints import service_orders, vehicles

api_router = APIRouter(redirect_slashes=False)

api_router.include_router(
    vehicles.router,
    prefix="/vehicles",
    tags=["vehicles"],
)

api_router.include_router(
    service_orders.router,
    prefix="/service_orders",
    tags=["service_orders"],
)

app = FastAPI()
app.include_router(api_router)
