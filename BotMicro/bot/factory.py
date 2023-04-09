import asyncio
from os import getenv, environ
from string import ascii_letters, digits
from random import choices

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram_deta.storage import DefaultKeyBuilder, DetaStorage
from deta import Deta

from bot.handlers import router as root_router
from bot.middlewares.logging import LoggingMiddleware
from bot.middlewares.callback_message import CallbackMessageMiddleware


def create_bot(token: str) -> tuple[Bot, str]:
    bot = Bot(token, parse_mode='HTML')

    webhook_url = getenv('DETA_SPACE_APP_HOSTNAME', '') + '/webhook'
    webhook_secret = ''.join(choices(ascii_letters + digits, k=32))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.set_webhook(url=webhook_url, secret_token=webhook_secret))

    return bot, webhook_secret


def create_dispatcher(deta: Deta) -> Dispatcher:
    base = deta.AsyncBase('fsm')  # type: ignore
    storage = DetaStorage(base, DefaultKeyBuilder(with_destiny=True))  # type: ignore

    dispatcher = Dispatcher(storage=storage)

    dispatcher.include_router(root_router)
    dispatcher.callback_query.middleware(CallbackMessageMiddleware())
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())

    if getenv('ENABLE_EVENTS_LOGS') == 'True':
        dispatcher.update.middleware(LoggingMiddleware())
        
    return dispatcher
