# project/app/config.py
# environment-specific configuration variables:

import logging
from functools import lru_cache

<<<<<<< HEAD
from pydantic import AnyUrl
=======
>>>>>>> 16e83fc342c710ba04d8ba3d5dbd5773072eea98
from pydantic_settings import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = 0
<<<<<<< HEAD
    database_url: AnyUrl = None
=======
>>>>>>> 16e83fc342c710ba04d8ba3d5dbd5773072eea98

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()