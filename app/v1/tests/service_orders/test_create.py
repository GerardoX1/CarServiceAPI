from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.v1.schemas.service_order import ServiceOrderCreate
from app.v1.tests.mocks.service_orders import (
    mock_response,
    mock_service_order_data,
)
from main import app

client = TestClient(app)


expected_service_order = ServiceOrderCreate(**mock_service_order_data)


def test_create_service_order():
    with patch(
        "app.v1.flows.services_orders.ServiceOrdersFlow.create",
        return_value=mock_response,
    ) as mock_create:
        with patch("app.libs.mongo_handler.get_repository") as mock_repo:
            mock_repo.return_value = MagicMock()

            response = client.post("/v1/service_orders", json=mock_service_order_data)

            mock_create.assert_called_once()
            called_args, called_kwargs = mock_create.call_args

            assert isinstance(called_kwargs["data"], ServiceOrderCreate)
            assert (
                called_kwargs["data"].model_dump()
                == expected_service_order.model_dump()
            )

            assert response.status_code == 201
            assert response.json()["data"] == mock_response
