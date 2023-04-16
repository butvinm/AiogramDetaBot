from os import getenv

from aiogram import Router
from aiogram.types.error_event import ErrorEvent

from utils.logging import log_to_deta

router = Router()


@router.errors()
async def errors_handler(event: ErrorEvent):
    expire_after_str = getenv('ERROR_LOGS_EXPIRE_AFTER')
    if expire_after_str is None or expire_after_str == '':
        expire_after = None
    else:
        expire_after = int(expire_after_str)

    await log_to_deta(
        data={
            'exception': repr(event.exception),
            'update': event.update.json()
        },
        expire_after=expire_after
    )
