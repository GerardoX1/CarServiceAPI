from httpx import Response
from pytest import mark
from starlette.testclient import TestClient


@mark.usefixtures("mocked_repository")
def test_health_check(client: TestClient):
    response: Response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "ready"
