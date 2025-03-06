from fastapi import APIRouter, Depends, Request, Response
from infra.mongo import MongoRepository
from presentation.status import Status

from app.libs.mongo_handler import get_repository
from app.v1.exceptions.handler import exception_handler
from app.v1.flows.services_orders import ServiceOrdersFlow
from app.v1.schemas.service_order import (
    QueryInput,
    ServiceOrderCreate,
    ServiceOrderPatch,
)

router = APIRouter()


# ? [POST] <— /v1/service_orders
@router.post("")
@exception_handler(response_status=Status.CREATED)
async def create_service_orders(
    request: Request,
    response: Response,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = ServiceOrdersFlow(repository=repository)
    parsed_model = ServiceOrderCreate.model_validate(await request.json())
    return flow.create(data=parsed_model)


# ? [GET] <— /v1/service_orders
@router.get("")
@exception_handler(response_status=Status.OK)
async def get_service_orders(
    request: Request,
    response: Response,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    query_params = QueryInput(**request.query_params)  # type: ignore
    flow = ServiceOrdersFlow(repository=repository)
    return flow.paginated_query(query_params)


# ? [GET] <— /v1/service_orders/{service_order_id}
@router.get("/{service_order_id}")
@exception_handler(response_status=Status.OK)
async def get_service_orders_by_id(
    request: Request,
    response: Response,
    service_order_id: str,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = ServiceOrdersFlow(repository=repository)
    return flow.get_by_id(service_order_id=service_order_id)


# ? [PATCH] <— /v1/service_orders/{service_order_id}
@router.patch("/{service_order_id}")
@exception_handler(response_status=Status.OK)
async def patch_service_order_id(
    request: Request,
    response: Response,
    service_order_id: str,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = ServiceOrdersFlow(repository=repository)
    parsed_model = ServiceOrderPatch.model_validate(await request.json())
    return flow.patch(service_order_id=service_order_id, data=parsed_model)


# ? [POST] <— /v1/service_orders/{service_order_id}/command/in_progress
@router.post("/{service_order_id}/command/in_progress")
@exception_handler(response_status=Status.OK)
async def in_progress(
    request: Request,
    response: Response,
    service_order_id: str,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = ServiceOrdersFlow(repository=repository)
    return flow.in_progress(service_order_id=service_order_id)


# ? [POST] <— /v1/service_orders/{service_order_id}/command/closed
@router.post("/{service_order_id}/command/closed")
@exception_handler(response_status=Status.OK)
async def closed(
    request: Request,
    response: Response,
    service_order_id: str,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = ServiceOrdersFlow(repository=repository)
    return flow.closed(service_order_id=service_order_id)


# ? [POST] <— /v1/service_orders/{service_order_id}/command/canceled
@router.post("/{service_order_id}/command/canceled")
@exception_handler(response_status=Status.OK)
async def canceled(
    request: Request,
    response: Response,
    service_order_id: str,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = ServiceOrdersFlow(repository=repository)
    return flow.canceled(service_order_id=service_order_id)
