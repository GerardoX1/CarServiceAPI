from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.v1.tests.mocks.service_orders import mock_service_orders_list
from main import app

client = TestClient(app)


def test_get_service_orders():
    with patch(
        "app.v1.flows.services_orders.ServiceOrdersFlow.paginated_query",
        return_value=mock_service_orders_list,
    ) as mock_query:
        with patch("app.libs.mongo_handler.get_repository") as mock_repo:
            mock_repo.return_value = MagicMock()

            response = client.get("/v1/service_orders")

            mock_query.assert_called_once()

            assert response.status_code == 200
            assert response.json()["data"] == mock_service_orders_list
