from fastapi import APIRouter

from robot33.routers import root
from robot33.routers.v1 import application, users, ai

router_root = root.router

router_v1 = APIRouter(prefix="/v1")

router_v1.include_router(application.router)
router_v1.include_router(users.router)
router_v1.include_router(ai.router)
