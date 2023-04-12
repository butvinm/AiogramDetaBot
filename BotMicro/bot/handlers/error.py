from datetime import datetime
from os import getenv

from aiogram import Router
from aiogram.types.error_event import ErrorEvent
from deta import Base

router = Router()


@router.errors()
async def errors_handler(event: ErrorEvent):
    time = datetime.now()

    try:
        expire_after = int(getenv('ERROR_LOGS_EXPIRE_AFTER', 0))
    except ValueError:
        expire_after = None
        
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
    