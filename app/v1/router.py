from fastapi import APIRouter, FastAPI

from .endpoints import users

api_router = APIRouter(redirect_slashes=False)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["user"],
)

app = FastAPI()
app.include_router(api_router)
