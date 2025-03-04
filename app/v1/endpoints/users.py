from fastapi import APIRouter, Depends, Request, Response
from infra.mongo import MongoRepository
from presentation.status import Status

from app.libs.mongo_handler import get_repository
from app.v1.exceptions.handler import exception_handler
from app.v1.flows.users import UserFlow

router = APIRouter()


# ? [POST] <— /v1/users
@router.post("")
@exception_handler(response_status=Status.OK)
async def post_users(
    request: Request,
    response: Response,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    flow = UserFlow(repository=repository)
    parsed_model = UserPost.model_validate(await request.json())
    return flow.create(data=parsed_model)


# ? [GET] <— /v1/users
@router.get("")
@exception_handler(response_status=Status.OK)
async def paginated_query_users(
    request: Request,
    response: Response,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    query_params = QueryInput(**request.query_params)
    flow = UserFlow(repository=repository)
    return flow.paginated_query(query_params)


# ? [PATCH] <— /v1/users
@router.patch("/{user_id}")
@exception_handler(response_status=Status.OK)
async def paginated_query_users(
    request: Request,
    response: Response,
    user_id: str,
    repository: MongoRepository = Depends(get_repository),
) -> dict:
    body = UserPatch(**await request.json())
    flow = UserFlow(repository=repository)
    return flow.update(user_id, body)
