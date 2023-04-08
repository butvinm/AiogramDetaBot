from aiogram import Bot, Dispatcher
from deta import Deta
from fastapi import FastAPI

from web.routers import root_router
from web.stubs import BotStub, DispatcherStub, SecretStub


def create_app(deta: Deta, bot: Bot, dispatcher: Dispatcher, webhook_secret: str) -> FastAPI:
    app = FastAPI(title='Bot')
    app.dependency_overrides.update({
        BotStub: lambda: bot,
        DispatcherStub: lambda: dispatcher,
        SecretStub: lambda: webhook_secret,
    })

    app.include_router(root_router)
    return app
