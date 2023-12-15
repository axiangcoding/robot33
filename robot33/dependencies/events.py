from loguru import logger

from robot33.internal.db import db


async def startup_event():
    logger.info("Starting up...")


async def __check_db_status__() -> bool:
    ret = await db.database.command("ping")
    return ret["ok"] == 1
