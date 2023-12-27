import motor.motor_asyncio
from beanie import init_beanie

from app.user.models.user import User


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db_name = "fastapi"

    await init_beanie(database=client[db_name], document_models=[User])
