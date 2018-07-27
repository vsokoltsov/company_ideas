from aiohttp import web
import pymongo
from db import dbclient
import bcrypt
import jwt
import ipdb

async def sign_in(request):
    data = await request.json()
    return web.json_response(data)

async def sign_up(request):
    try:
        data = await request.post()
        salt = bcrypt.gensalt()
        password_digest = bcrypt.hashpw(
            data.get('password').encode('utf8'), salt
        )
        user = {
            'email': data.get('email'),
            'password_digest': password_digest
        }
        result = await dbclient.users.insert_one(user)
        encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
        return web.json_response({ 'success': 'true' })
    except pymongo.errors.DuplicateKeyError as e:
        return web.json_response(e.args[0])
    except Exception as e:
        print('EXCEPTION', e)

async def current_user(request):
    return web.json_response(request)
