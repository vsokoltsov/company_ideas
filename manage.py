import fire
import sys
import ipdb
import os
import unittest

from app import AppServer
from app.config import APP_ENV, TEST


def start():
    """Start development server."""

    server = AppServer()
    server.run()


def test(path=None):
    """Run tests."""
    ipdb.set_trace()
    os.environ[APP_ENV] = TEST
    if path is None:
        tests = unittest.TestLoader().discover('tests', pattern='*.py')
    else:
        tests = unittest.TestLoader().loadTestsFromName(path)
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    fire.Fire()
