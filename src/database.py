import motor.motor_asyncio
from beanie import init_beanie
from src.config import settings
from src.users.models import User


MONGO_CONFIG_URL=f"mongodb://{settings.mongo_username}:{settings.mongo_password}@{settings.mongo_host}:{settings.mongo_port}/"

# ME_CONFIG_MONGODB_URL: "mongodb://${MONGO_USERNAME}:${MONGO_PASSWORD}@${EXPRESS_MONGO_HOST}:${MONGO_PORT}/"


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_CONFIG_URL)
    await init_beanie(database=client[settings.mongo_database], document_models=[User])
