from traxion.models.v1.vehicles import VehicleModel

from app.v1.flows._base_flow import Flow
from app.v1.schemas.vehicles import VehiclesCreate, VehiclesPatch


class VehiclesFlow(Flow):
    def create(
        self,
        data: VehiclesCreate,
    ) -> dict:
        """
        Function to create vehicles.

        :return: content to be returned into response.
        :rtype: dict
        """
        vehicle: VehicleModel = VehicleModel(**data.model_dump())
        model = self._service.create(vehicle)  # type: ignore
        return {VehicleModel.__collection_name__: model.model_dump(by_alias=True)}

    def patch(
        self,
        vehicle_id: str,
        data: VehiclesPatch,
    ) -> dict:
        """
        Function to patch vehicles.
        data: VehiclesPatch,

        :return: content to be returned into response.
        :rtype: dict
        """
        model_vecicle: VehicleModel = self._get_vehicle(vehicle_id)
        model = model_vecicle.updated_copy(data.model_dump(exclude=None))
        return {VehicleModel.__collection_name__: model.model_dump(by_alias=True)}
