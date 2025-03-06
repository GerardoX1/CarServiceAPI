from datetime import datetime

BASE_SERVICE_ORDER_ID = "e5bd15df-8374-47d0-8033-40e81a7d13ee"
BASE_VEHICLE_ID = "fbb0517d-9a86-433e-b24c-ba8e675c052b"
BASE_DESCRIPTION = "Alguien puso jugo de naranja en deposito de gasolina"
BASE_SERVICE_TYPE = "CORRECTIVE"
BASE_VERSION = "1.0.0"
BASE_TIMESTAMP = int(datetime.now().timestamp() * 1000)


def generate_mock_service_order(status, updated_at=None, description=BASE_DESCRIPTION):
    return {
        "service_orders": {
            "updated_at": updated_at if updated_at else BASE_TIMESTAMP,
            "_id": BASE_SERVICE_ORDER_ID,
            "created_at": 1741297340174,
            "version": BASE_VERSION,
            "vehicle_id": BASE_VEHICLE_ID,
            "service_type": BASE_SERVICE_TYPE,
            "description": description,
            "status": status,
        }
    }


mock_service_order_data = {
    "vehicle_id": BASE_VEHICLE_ID,
    "service_type": BASE_SERVICE_TYPE,
    "description": BASE_DESCRIPTION,
}

mock_response = generate_mock_service_order(status="CREATED")

mock_service_orders_list = {
    "service_orders": [generate_mock_service_order(status="CREATED")["service_orders"]],
    "page_limit": 50,
    "total_pages": 1,
    "items_count": 1,
}

mock_service_order_detail = generate_mock_service_order(
    status="CREATED", description="se desconchinflo la cosa esa"
)
mock_service_order_in_progress = generate_mock_service_order(
    status="IN_PROGRESS", updated_at=BASE_TIMESTAMP + 1000
)
mock_service_order_closed = generate_mock_service_order(
    status="CLOSED", updated_at=BASE_TIMESTAMP + 2000
)
mock_service_order_canceled = generate_mock_service_order(
    status="CANCELED", updated_at=BASE_TIMESTAMP + 3000
)
