from os import getenv

from aiogram import Router
from aiogram.types.error_event import ErrorEvent
from utils.env_parse import parse_expire_after

from utils.logging import log_to_deta

router = Router()


@router.errors()
async def errors_handler(event: ErrorEvent):
    expire_after = parse_expire_after(getenv('ERROR_LOGS_EXPIRE_AFTER', ''))
    
    await log_to_deta(
        data={
            'exception': repr(event.exception),
            'update': event.update.json()
        },
        expire_after=expire_after
    )
