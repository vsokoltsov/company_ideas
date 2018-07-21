import os
from app.utils import get_env_variable

from .development import ConfigDevelopment
from .test import ConfigTest

APP_ENV = 'APP_ENV'
DEVELOPMENT = 'development'
TEST = 'test'


def get_actual_environment():
    """Return config class based on environment variable."""
    env = os.environ.get(APP_ENV, DEVELOPMENT)
    if env == TEST:
        return ConfigTest
    else:
        return ConfigDevelopment
