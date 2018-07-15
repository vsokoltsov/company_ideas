import asyncio
import motor.motor_asyncio

async def create_user_unique_index(client):
    return await client.users.create_index('email', unique=True)

async def create_user_collection(client):
    try:
        return await client.create_collection('users')
    except:
        pass

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:root@mongo:27017')
dbclient = client.client_ideas
asyncio.ensure_future(create_user_collection(dbclient))
asyncio.ensure_future(create_user_unique_index(dbclient))
