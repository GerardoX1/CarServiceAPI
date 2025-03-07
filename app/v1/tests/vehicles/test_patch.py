from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.v1.schemas.vehicles import VehiclesPatch
from app.v1.tests.mocks.vehicles import (
    mock_vehicle_patch_data,
    mock_vehicle_updated_response,
)
from main import app

client = TestClient(app)


def test_patch_vehicle():
    vehicle_id = "cc40aa76-8381-419c-b5cb-37e708556ab7"

    with patch(
        "app.v1.flows.vehicles.VehiclesFlow.patch",
        return_value=mock_vehicle_updated_response,
    ) as mock_patch:
        with patch("app.libs.mongo_handler.get_repository") as mock_repo:
            mock_repo.return_value = MagicMock()

            response = client.patch(
                f"/v1/vehicles/{vehicle_id}", json=mock_vehicle_patch_data
            )

            mock_patch.assert_called_once()
            called_args, called_kwargs = mock_patch.call_args

            assert isinstance(called_kwargs["data"], VehiclesPatch)
            assert (
                called_kwargs["data"].model_dump(exclude_unset=True)
                == mock_vehicle_patch_data
            )

            assert response.status_code == 200
            assert response.json()["data"] == mock_vehicle_updated_response
