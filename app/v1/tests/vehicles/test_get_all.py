from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.v1.tests.mocks.vehicles import mock_vehicles_list
from main import app

client = TestClient(app)


def test_get_all_vehicles():
    with patch(
        "app.v1.flows.vehicles.VehiclesFlow.paginated_query",
        return_value=mock_vehicles_list,
    ) as mock_query:
        with patch("app.libs.mongo_handler.get_repository") as mock_repo:
            mock_repo.return_value = MagicMock()

            response = client.get("/v1/vehicles/")
            mock_query.assert_called_once()

            assert response.status_code == 200
            assert response.json()["data"] == mock_vehicles_list
