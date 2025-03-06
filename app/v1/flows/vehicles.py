from math import ceil

from traxion.models.v1.vehicles import VehicleModel

from app.v1.flows._base_flow import Flow
from app.v1.schemas.vehicles import QueryInput, VehiclesCreate, VehiclesPatch


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
        model = self._service_vehicle.create(vehicle)  # type: ignore
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
        model = model_vecicle.updated_copy(data.model_dump(exclude_unset=True))
        return {VehicleModel.__collection_name__: model.model_dump(by_alias=True)}

    def get_by_id(
        self,
        vehicle_id: str,
    ) -> dict:
        """
        Function to get vehicles.

        :return: content to be returned into response.
        :rtype: dict
        """
        model: VehicleModel = self._get_vehicle(vehicle_id)
        return {VehicleModel.__collection_name__: model.model_dump(by_alias=True)}

    def paginated_query(self, query_params: QueryInput) -> dict:
        count, vehicles = self._service_vehicle.paginated_query(
            page=query_params.page,
            limit=query_params.limit,
            conditions=query_params.filters(),
            sort=query_params.sort,
        )
        response = {"vehicles": vehicles}
        if vehicles:
            response.update(
                {
                    "page_limit": query_params.limit,
                    "total_pages": ceil(count / query_params.limit),
                    "items_count": count,
                }
            )
        return response
