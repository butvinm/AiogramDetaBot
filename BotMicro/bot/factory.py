from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram_deta.storage import DefaultKeyBuilder, DetaStorage
from deta import Deta

from bot.handlers import router as root_router
from bot.middlewares.logging import LoggingMiddleware
from utils.env_parse import parse_bool, parse_optional_int


def create_bot(token: str) -> Bot:
    bot = Bot(token, parse_mode='HTML')
    return bot


def create_dispatcher(deta: Deta) -> Dispatcher:
    base = deta.AsyncBase('fsm')  # type: ignore
    storage = DetaStorage(base, DefaultKeyBuilder(with_destiny=True))  # type: ignore

    dispatcher = Dispatcher(storage=storage)

    dispatcher.include_router(root_router)
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())

    if parse_bool(getenv('ENABLE_EVENTS_LOGS', 'false')):
        expire_after = parse_optional_int(getenv('EVENTS_LOGS_EXPIRE_AFTER', ''))
        dispatcher.update.middleware(LoggingMiddleware(expire_after))

    return dispatcher
