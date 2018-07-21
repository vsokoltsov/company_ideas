from aiohttp.test_utils import AioHTTPTestCase
from app import AppServer
import ipdb


class BaseTestCase(AioHTTPTestCase):
    """Base test class."""

    async def get_application(self):
        """Return application instance for test environment."""

        server = AppServer()
        return server.app
