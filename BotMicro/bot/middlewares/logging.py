from datetime import datetime
from typing import Any, Awaitable, Callable, Dict

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject
from deta import Base  # type: ignore


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        time = datetime.now()

        logging_base = Base('logs')
        logging_base.put(
            key=str(2 * 10**9 - time.timestamp()),
            data={'time': time.isoformat(), 'update': event.json()},
            expire_in=60 * 60 * 2  # expire in two hours
        )

        return await handler(event, data)
