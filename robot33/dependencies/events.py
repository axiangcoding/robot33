from loguru import logger

from robot33.internal.db import db


async def startup_event():
    logger.info("Starting up...")
