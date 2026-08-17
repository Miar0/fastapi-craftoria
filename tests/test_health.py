import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
class TestHealthCheck:
    async def test_health_check_returns_200(self, client: AsyncClient) -> None:
        response = await client.get("/api/v1/health")

        assert response.status_code == 200
        assert response.json() == {"status": "ok", "database": "connected"}

    async def test_health_check_response_structure(self, client: AsyncClient) -> None:
        response = await client.get("/api/v1/health")

        data = response.json()
        assert "status" in data
        assert "database" in data
