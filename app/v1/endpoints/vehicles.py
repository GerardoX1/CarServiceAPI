from fastapi import APIRouter, Depends, Request, Response
from infra.mongo import MongoRepository
from presentation.status import Status

from app.libs.mongo_handler import get_repository
from app.v1.exceptions.handler import exception_handler
from app.v1.flows.vehicles import VehiclesFlow
from app.v1.schemas.vehicles import QueryInput, VehiclesCreate, VehiclesPatch

router = APIRouter()


# ? [POST] <— /v1/vehicles
@router.post("")
@exception_handler(response_status=Status.CREATED)
async def create_vehicles(
    request: Request,
    response: Response,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = VehiclesFlow(repository=repository)
    parsed_model = VehiclesCreate.model_validate(await request.json())
    return flow.create(data=parsed_model)


# ? [GET] <— /v1/vehicles
@router.get("")
@exception_handler(response_status=Status.OK)
async def get_vehicles(
    request: Request,
    response: Response,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    query_params = QueryInput(**request.query_params)  # type: ignore
    flow = VehiclesFlow(repository=repository)
    return flow.paginated_query(query_params)


# ? [GET] <— /v1/vehicles/{vehicle_id}
@router.get("/{vehicle_id}")
@exception_handler(response_status=Status.OK)
async def get_vehicles_by_id(
    request: Request,
    response: Response,
    vehicle_id: str,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = VehiclesFlow(repository=repository)
    return flow.get_by_id(vehicle_id=vehicle_id)


# ? [PATCH] <— /v1/vehicles/{vehicle_id}
@router.patch("/{vehicle_id}")
@exception_handler(response_status=Status.OK)
async def patch_vehicles(
    request: Request,
    response: Response,
    vehicle_id: str,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = VehiclesFlow(repository=repository)
    parsed_model = VehiclesPatch.model_validate(await request.json())
    return flow.patch(vehicle_id=vehicle_id, data=parsed_model)
