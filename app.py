from aiohttp import web
import ipdb

async def hello(request):
    return web.Response(text="Hello, world")

async def sign_in(request):
    data = await request.json()
    return web.json_response(data)

async def sign_up(request):
    data = await request.json()
    return web.json_response(data)

async def current_user(request):
    return web.json_response(request)


def start(args):
    app = web.Application()
    app.add_routes([
        web.get('/', hello),
        web.post('/sign_in', sign_in),
        web.post('/sign_up', sign_up),
        web.get('/current_user', current_user)
    ])
    web.run_app(app, port=8000)
