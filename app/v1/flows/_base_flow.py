from typing import Optional

from infra.mongo import MongoRepository
from presentation.error import NotFoundError
from traxion.services.v1.service_orders import (
    ServiceOrderModel,
    ServiceOrderService,
)
from traxion.services.v1.vehicles import VehicleModel, VehicleService


class Flow:
    def __init__(self, repository: MongoRepository):
        self._repository = repository
        self._service_vehicle: VehicleService = VehicleService(repository)
        self._service_order: ServiceOrderService = ServiceOrderService(repository)

    def _get_vehicle(
        self,
        vehicle_id: str,
    ) -> VehicleModel:
        model: Optional[VehicleModel] = self._service_vehicle.get(vehicle_id)
        if not model:
            raise NotFoundError(
                location=NotFoundError.ERROR_LOCATION.PATH,
                parameter="vehicle_id",
                details=f"The vehicle with id '{vehicle_id}' was not found.",
                displayable_message="El vehículo que intentas buscar no existe.",
            )
        return model

    def _get_service_order(
        self,
        service_order_id: str,
    ) -> ServiceOrderModel:
        model: Optional[ServiceOrderModel] = self._service_order.get(service_order_id)
        if not model:
            raise NotFoundError(
                location=NotFoundError.ERROR_LOCATION.PATH,
                parameter="service_order_id",
                details=f"The service vehicle with id '{service_order_id}' was not found.",
                displayable_message="La orden de servicio que intentas buscar no existe.",
            )
        return model
