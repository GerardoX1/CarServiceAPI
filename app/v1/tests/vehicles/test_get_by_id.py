from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.v1.tests.mocks.vehicles import mock_vehicle_detail
from main import app

client = TestClient(app)


def test_get_vehicle_by_id():
    vehicle_id = "cc40aa76-8381-419c-b5cb-37e708556ab7"

    with patch(
        "app.v1.flows.vehicles.VehiclesFlow.get_by_id", return_value=mock_vehicle_detail
    ) as mock_get_by_id:
        with patch("app.libs.mongo_handler.get_repository") as mock_repo:
            mock_repo.return_value = MagicMock()

            response = client.get(f"/v1/vehicles/{vehicle_id}")
            mock_get_by_id.assert_called_once_with(vehicle_id=vehicle_id)

            assert response.status_code == 200
            assert response.json()["data"] == mock_vehicle_detail
