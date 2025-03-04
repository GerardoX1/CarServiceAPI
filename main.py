import uvicorn
from fastapi import FastAPI

from app.libs import mongo_handler
from app.v1.router import app as v1_app

app = FastAPI()

app.add_event_handler("startup", mongo_handler.open_connection)
app.add_event_handler("shutdown", mongo_handler.close_connection)

app.mount("/v1", v1_app)


@app.get("/")
async def health_check():
    return "ready"


if __name__ == "__main__":
    uvicorn.run(app, port=8080)  # pragma: no cover
