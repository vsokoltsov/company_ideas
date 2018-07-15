from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from app import get_app

class AuthorizationViewTests(AioHTTPTestCase):

    async def get_application(self):
        return get_app()

    @unittest_run_loop
    async def test_success_sign_up(self):
        data = {
            'email': 'example@mail.com',
            'password': '123456'
        }
        resp = await self.client.post('/sign_up', data=data)
