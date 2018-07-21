from . import get_env_variable


class ConfigDevelopment:
    """Development configuration file."""

    COLLECTION = get_env_variable('MONGO_INITDB_DATABASE')
