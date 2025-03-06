from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.v1.tests.mocks.service_orders import mock_service_order_detail
from main import app

client = TestClient(app)


def test_get_service_order_by_id():
    service_order_id = "e5bd15df-8374-47d0-8033-40e81a7d13ee"

    with patch(
        "app.v1.flows.services_orders.ServiceOrdersFlow.get_by_id",
        return_value=mock_service_order_detail,
    ) as mock_get_by_id:
        with patch("app.libs.mongo_handler.get_repository") as mock_repo:
            mock_repo.return_value = MagicMock()

            response = client.get(f"/v1/service_orders/{service_order_id}")

            mock_get_by_id.assert_called_once_with(service_order_id=service_order_id)

            assert response.status_code == 200
            assert response.json()["data"] == mock_service_order_detail
