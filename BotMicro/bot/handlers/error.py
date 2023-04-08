from datetime import datetime

from aiogram import Router
from aiogram.types.error_event import ErrorEvent
from deta import Base

router = Router()


@router.errors()
async def errors_handler(event: ErrorEvent):
    time = datetime.now()

    logging_base: _Base = Base('logs')
    logging_base.put(
        key=str(2 * 10**9 - time.timestamp()),
        data={
            'time': time.isoformat(), 
            'exception': repr(event.exception),
            'update': event.update.json()
        }
    )
    