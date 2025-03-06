from pydantic import BaseModel, PositiveInt
from traxion.models.v1.vehicles import StatusVehicle


class VehiclesCreate(BaseModel):
    plate_number: str
    brand: str
    model: str
    year: PositiveInt
    mileage: PositiveInt
    status: list[StatusVehicle]


class VehiclesPatch(BaseModel):
    brand: str
    model: str
    year: PositiveInt
    mileage: PositiveInt
