import os


def get_env_variable(key):
    """Return environemnt variable."""

    try:
        return os.environ[key]
    except KeyError:
        raise ValueError('{} does not exit in .env file'.format(key))
