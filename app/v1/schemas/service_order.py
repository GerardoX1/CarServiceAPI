from typing import Optional

from presentation.error import ErrorLocationEnum
from pydantic import BaseModel, Field
from traxion.models.base_models.queryable_model import QueryableModel
from traxion.models.v1.service_orders import ServiceStatusType, ServiceType


class QueryInput(QueryableModel):
    __location__ = ErrorLocationEnum.QUERY

    created_gt: Optional[int] = Field(
        alias="created_at",
        default=None,
        json_schema_extra={"filter": True, "condition": ">="},
    )
    created_lt: Optional[int] = Field(
        alias="created_at",
        default=None,
        json_schema_extra={"filter": True, "condition": "<="},
    )


class ServiceOrderCreate(BaseModel):
    vehicle_id: str
    service_type: ServiceType
    description: str
    status: ServiceStatusType = Field(default=ServiceStatusType.CREATED)


class ServiceOrderPatch(BaseModel):
    service_type: Optional[ServiceType] = None
    description: Optional[str] = None
