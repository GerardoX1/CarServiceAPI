from typing import Optional

from presentation.error import ErrorLocationEnum
from pydantic import BaseModel, Field, PositiveInt
from traxion.models.base_models.queryable_model import QueryableModel
from traxion.models.v1.vehicles import StatusVehicle


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


class VehiclesCreate(BaseModel):
    plate_number: str
    brand: str
    model: str
    year: PositiveInt
    mileage: PositiveInt
    status: StatusVehicle


class VehiclesPatch(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    year: Optional[PositiveInt] = None
    mileage: Optional[PositiveInt] = None
