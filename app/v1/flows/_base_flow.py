from typing import Optional

from infra.mongo import MongoRepository
from presentation.error import NotFoundError
from traxion.services.v1.vehicles import VehicleModel, VehicleService


class Flow:
    def __init__(self, repository: MongoRepository):
        self._repository = repository
        self._service: VehicleService = VehicleService(repository)

    def _get_vehicle(
        self,
        vehicle_id: str,
    ) -> VehicleModel:
        model: Optional[VehicleModel] = self._service.get(vehicle_id)
        if not model:
            raise NotFoundError(
                location=NotFoundError.ERROR_LOCATION.PATH,
                parameter="vehicle_id",
                details=f"The vehicle with id '{vehicle_id}' was not found.",
                displayable_message="El vehículo que intentas buscar no existe.",
            )
        return model
