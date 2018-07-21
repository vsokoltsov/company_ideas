from . import get_env_variable


class ConfigDevelopment:
    """Development configuration file."""

    DB_NAME = get_env_variable('MONGO_INITDB_DATABASE', 'company_ideas_dev')
