from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.types.error_event import ErrorEvent
from fastapi import APIRouter, Depends, Header, HTTPException, status
from pydantic import SecretStr

from web.stubs import BotStub, DispatcherStub, SecretStub

webhook_router = APIRouter(prefix='/webhook', tags=['Webhook'])


@webhook_router.post('')
async def feed_update(
    update: Update,
    secret: SecretStr = Header(alias='X-Telegram-Bot-Api-Secret-Token'),
    expected_secret: str = Depends(SecretStub),
    bot: Bot = Depends(BotStub),
    dispatcher: Dispatcher = Depends(DispatcherStub),
):
    if secret.get_secret_value() != expected_secret:
        raise HTTPException(detail='Invalid secret', status_code=status.HTTP_401_UNAUTHORIZED)

    result = await dispatcher.feed_update(bot, update=update)
    if isinstance(result, ErrorEvent):
        return {'ok': False, 'exception': result.exception, 'dispatcher': result}

    return {'ok': True, 'dispatcher': result}
