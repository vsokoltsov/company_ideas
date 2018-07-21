from aiohttp import web
from app.db import dbclient

from app.api import objects


class AppServer:
    """App server class."""

    def __init__(self, end=None):
        """Set default ."""

        self.app = web.Application()
        self.db = dbclient
        self.app.add_routes(objects)

    def run(self):
        """Run aiohttp server."""

        web.run_app(self.app, port=8000)
