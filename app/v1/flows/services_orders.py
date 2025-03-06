from math import ceil

from traxion.models.v1.service_orders import (
    ServiceOrderModel,
    ServiceStatusType,
)

from app.v1.flows._base_flow import Flow
from app.v1.schemas.service_order import (
    QueryInput,
    ServiceOrderCreate,
    ServiceOrderPatch,
)


class ServiceOrdersFlow(Flow):
    def create(
        self,
        data: ServiceOrderCreate,
    ) -> dict:
        """
        Function to create services vehicles.

        :return: content to be returned into response.
        :rtype: dict
        """
        services_vehicle: ServiceOrderModel = ServiceOrderModel(**data.model_dump())
        model = self._service_order.create(services_vehicle)  # type: ignore
        return {ServiceOrderModel.__collection_name__: model.model_dump(by_alias=True)}

    def patch(
        self,
        service_order_id: str,
        data: ServiceOrderPatch,
    ) -> dict:
        """
        Function to patch vehicles.
        data: ServiceOrderPatch,

        :return: content to be returned into response.
        :rtype: dict
        """
        model_services_vecicle: ServiceOrderModel = self._get_service_order(
            service_order_id
        )
        model = model_services_vecicle.updated_copy(data.model_dump(exclude_unset=True))
        return {ServiceOrderModel.__collection_name__: model.model_dump(by_alias=True)}

    def get_by_id(
        self,
        service_order_id: str,
    ) -> dict:
        """
        Function to get service_vehicle.

        :return: content to be returned into response.
        :rtype: dict
        """
        model: ServiceOrderModel = self._get_service_order(service_order_id)
        return {ServiceOrderModel.__collection_name__: model.model_dump(by_alias=True)}

    def paginated_query(self, query_params: QueryInput) -> dict:
        count, service_vehicles = self._service_order.paginated_query(
            page=query_params.page,
            limit=query_params.limit,
            conditions=query_params.filters(),
            sort=query_params.sort,
        )
        response = {ServiceOrderModel.__collection_name__: service_vehicles}
        if service_vehicles:
            response.update(
                {
                    "page_limit": query_params.limit,
                    "total_pages": ceil(count / query_params.limit),
                    "items_count": count,
                }
            )
        return response

    def in_progress(
        self,
        service_order_id: str,
    ) -> dict:
        """
        Function to in_progress vehicles.

        :return: content to be returned into response.
        :rtype: dict
        """
        model_services_vecicle: ServiceOrderModel = self._get_service_order(
            service_order_id
        )
        model = model_services_vecicle.updated_copy(
            {"status": ServiceStatusType.IN_PROGRESS}
        )
        return {ServiceOrderModel.__collection_name__: model.model_dump(by_alias=True)}

    def closed(
        self,
        service_order_id: str,
    ) -> dict:
        """
        Function to closed vehicles.

        :return: content to be returned into response.
        :rtype: dict
        """
        model_services_vecicle: ServiceOrderModel = self._get_service_order(
            service_order_id
        )
        model = model_services_vecicle.updated_copy(
            {"status": ServiceStatusType.CLOSED}
        )
        return {ServiceOrderModel.__collection_name__: model.model_dump(by_alias=True)}

    def canceled(
        self,
        service_order_id: str,
    ) -> dict:
        """
        Function to CANCELED vehicles.

        :return: content to be returned into response.
        :rtype: dict
        """
        model_services_vecicle: ServiceOrderModel = self._get_service_order(
            service_order_id
        )
        model = model_services_vecicle.updated_copy(
            {"status": ServiceStatusType.CANCELED}
        )
        return {ServiceOrderModel.__collection_name__: model.model_dump(by_alias=True)}
