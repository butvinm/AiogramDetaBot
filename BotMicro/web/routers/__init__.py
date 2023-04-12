from fastapi import APIRouter
from .webhook import webhook_router
from .info import info_router
from fastapi.responses import RedirectResponse

__all__ = ['root_router']


root_router = APIRouter()
root_router.include_router(webhook_router)
root_router.include_router(info_router)


@root_router.get('/')
async def root():
    return RedirectResponse(url='/info')
