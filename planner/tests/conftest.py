import asyncio

import httpx
import pytest

from database.connection import Settings
from main import app
from models.events import Event
from models.users import User

# 비동기 처리를 위한 코드
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

#DB 불러오기
async def init_db():
    test_settings = Settings()
    # test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"
    test_settings.DATABASE_NAME = "testdb"

    await test_settings.initialize_database()


@pytest.fixture(scope="session")
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client

        # Clean up resources
        await Event.find_all().delete()
        await User.find_all().delete()
        