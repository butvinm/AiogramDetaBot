from fastapi import APIRouter
from .webhook import webhook_router

__all__ = ['root_router']


root_router = APIRouter()
root_router.include_router(webhook_router)
