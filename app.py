from aiohttp import web
import pymongo
from db import dbclient
import bcrypt
import ipdb

async def hello(request):
    users = dbclient.users.find()
    collection = await users.to_list(length=100)
    return web.Response(text="Hello, world")

async def sign_in(request):
    data = await request.json()
    return web.json_response(data)

async def sign_up(request):
    data = await request.json()
    salt = bcrypt.gensalt()
    password_digest = bcrypt.hashpw(data.get('password'), salt)
    user = {
        'email': data.get('email'),
        'password_digest': password_digest
    }
    try:
        result = await dbclient.users.insert_one(user)
        ipdb.set_trace()
        return web.json_response(result)
    except pymongo.errors.DuplicateKeyError as e:
        return web.json_response(e.args[0])

async def current_user(request):
    return web.json_response(request)

def get_app():
    app = web.Application()
    app.add_routes([
        web.get('/', hello),
        web.post('/sign_in', sign_in),
        web.post('/sign_up', sign_up),
        web.get('/current_user', current_user)
    ])
    return app

def start(args):
    web.run_app(get_app(), port=8000)
