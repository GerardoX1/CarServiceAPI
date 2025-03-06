from fastapi import APIRouter, FastAPI

from .endpoints import vehicles

api_router = APIRouter(redirect_slashes=False)

api_router.include_router(
    vehicles.router,
    prefix="/vehicles",
    tags=["vehicles"],
)

app = FastAPI()
app.include_router(api_router)
