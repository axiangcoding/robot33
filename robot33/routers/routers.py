from fastapi import APIRouter

from robot33.routers.v1 import application, users

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(application.router)
router_v1.include_router(users.router)
