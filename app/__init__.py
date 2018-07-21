from aiohttp import web

from app.api import objects
import ipdb


class AppServer:
    """App server class."""

    def __init__(self, env=None):
        """Set default."""

        self.app = web.Application()
        self.app.add_routes(objects)

    def run(self):
        """Run aiohttp server."""

        web.run_app(self.app, port=8000)
