from aiogram import Bot
from fastapi import APIRouter, Depends

from web.stubs import BotStub, SecretStub

info_router = APIRouter(prefix='/info', tags=['Info'])


@info_router.get('')
async def get_bot_info(
    webhook_secret: str = Depends(SecretStub),
    bot: Bot = Depends(BotStub),
):
    webhook_info = await bot.get_webhook_info()
    return {
        'ok': True,
        'webhook_url': webhook_info.url,
        'webhook_secret': webhook_secret,
        'webhook_last_error_date': webhook_info.last_error_date,
        'webhook_last_error_message': webhook_info.last_error_message,
    }
