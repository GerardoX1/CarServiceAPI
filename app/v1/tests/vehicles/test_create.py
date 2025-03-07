from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.v1.schemas.vehicles import VehiclesCreate
from app.v1.tests.mocks.vehicles import mock_vehicle_data, mock_vehicle_response
from main import app

client = TestClient(app)


def test_create_vehicle():
    with patch(
        "app.v1.flows.vehicles.VehiclesFlow.create", return_value=mock_vehicle_response
    ) as mock_create:
        with patch("app.libs.mongo_handler.get_repository") as mock_repo:
            mock_repo.return_value = MagicMock()

            response = client.post("/v1/vehicles", json=mock_vehicle_data)

            mock_create.assert_called_once()
            called_args, called_kwargs = mock_create.call_args
            assert isinstance(called_kwargs["data"], VehiclesCreate)
            assert called_kwargs["data"].model_dump() == mock_vehicle_data

            assert response.status_code == 201
            assert response.json()["data"] == mock_vehicle_response
