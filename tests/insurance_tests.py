import pytest
import asyncio
from httpx import AsyncClient
from asgi_lifespan import LifespanManager

from src.main import app


@pytest.fixture(scope="module")
async def client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as c:
            yield c


@pytest.fixture(scope="session")
def event_loop():
    """Overrides pytest default function scoped event loop"""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


# Test calculate_insurance with negative declared value
@pytest.mark.asyncio
async def test_calculate_insurance_negative_declared_value(client: AsyncClient):
    data = {
        "declared_value": -100,
        "cargo_type": "Electronics"
    }
    response = await client.post("/api/insurance/calculate", json=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Declared value must be greater than 0"


# Test calculate_insurance with declared value exceeding maximum
@pytest.mark.asyncio
async def test_calculate_insurance_exceed_max_declared_value(client: AsyncClient):
    data = {
        "declared_value": 1_000_001,
        "cargo_type": "Electronics"
    }
    response = await client.post("/api/insurance/calculate", json=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Declared value must be between 500 and 1 million"


# # Test calculate_insurance with declared value below minimum
@pytest.mark.asyncio
async def test_calculate_insurance_below_min_declared_value(client: AsyncClient):
    data = {
        "declared_value": 499,
        "cargo_type": "Electronics"
    }
    response = await client.post("/api/insurance/calculate", json=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "Declared value must be between 500 and 1 million"


# # Test calculate_insurance with declared value equal to minimum
@pytest.mark.asyncio
async def test_calculate_insurance_min_declared_value(client: AsyncClient):
    data = {
        "declared_value": 500,
        "cargo_type": "Electronics"
    }
    response = await client.post("/api/insurance/calculate", json=data)

    assert response.status_code == 200
    assert "cost_insurance" in response.json()


# # Test calculate_insurance with declared value equal to zero
@pytest.mark.asyncio
async def test_calculate_insurance_zero_declared_value(client: AsyncClient):
    data = {
        "declared_value": 0,
        "cargo_type": "Electronics"
    }
    response = await client.post("/api/insurance/calculate", json=data)

    assert response.status_code == 400
    assert response.json()["detail"] == "One or more field(s) is empty"


# # Test calculate_insurance with non-existent cargo type
@pytest.mark.asyncio
async def test_calculate_insurance_invalid_cargo_type(client: AsyncClient):
    data = {
        "declared_value": 1000,
        "cargo_type": "InvalidType"
    }
    response = await client.post("/api/insurance/calculate", json=data)

    assert response.status_code == 404
    assert response.json()["detail"] == "Enter one of the suggested cargo-type - [Electronics, Furniture, Chemicals, Other]"
