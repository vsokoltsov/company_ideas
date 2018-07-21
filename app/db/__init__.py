import asyncio
import motor.motor_asyncio

from app.config import get_actual_environment

env = get_actual_environment()


async def create_user_unique_index(client):
    """Create unique index for the user."""

    return await client.users.create_index('email', unique=True)


async def create_user_collection(client):
    """Create user collection."""

    try:
        return await client.create_collection('users')
    except Exception:
        pass

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb://root:root@mongo:27017'
)
dbclient = client[env.COLLECTION]
asyncio.ensure_future(create_user_collection(dbclient))
asyncio.ensure_future(create_user_unique_index(dbclient))