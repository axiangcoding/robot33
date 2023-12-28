from fastapi import FastAPI

from robot33 import config, logging
from robot33.dependencies import error_handler, events
from robot33.routers import routers

logging.setup_logging()
settings = config.get_settings()
app = FastAPI(
    title=settings.app.name,
    version=settings.app.version,
    description=settings.app.description,
    debug=settings.app.debug,
)

app.add_exception_handler(Exception, error_handler.global_exception_handler)

app.add_event_handler("startup", events.startup_event)

app.include_router(routers.router_root)
app.include_router(routers.router_v1)
