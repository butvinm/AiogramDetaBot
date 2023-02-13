from aiogram import Dispatcher

from bot import handlers


def register_routers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(handlers.router)
