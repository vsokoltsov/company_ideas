from aiohttp import web

from .v1 import *

objects = [
    web.post('/api/v1/sign_in', sign_in),
    web.post('/api/v1/sign_up', sign_up),
    web.get('/api/v1/current_user', current_user)
]
