from datetime import datetime
from os import getenv

from aiogram import Router
from aiogram.types.error_event import ErrorEvent
from deta import Base

router = Router()


@router.errors()
async def errors_handler(event: ErrorEvent):
    time = datetime.now()

    expire_after_str = getenv('ERROR_LOGS_EXPIRE_AFTER')
    if expire_after_str is None or expire_after_str == '':
        expire_after = None
    else:
        expire_after = int(expire_after_str)
        
    logging_base = Base('logs')
    logging_base.put(
        key=str(2 * 10**9 - time.timestamp()),
        data={
            'time': time.isoformat(), 
            'exception': repr(event.exception),
            'update': event.update.json()
        },
        expire_in=expire_after
    )
    