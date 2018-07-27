from aiohttp.test_utils import unittest_run_loop
from tests.base import BaseTestCase
import ipdb

class AuthorizationViewTests(BaseTestCase):

    @unittest_run_loop
    async def test_success_sign_up(self):
        data = {
            'email': 'example@mail.com',
            'password': '123456'
        }
        resp = await self.client.post('/api/v1/sign_up', data=data)
