from datetime import datetime
from typing import Any, Awaitable, Callable, Dict, Optional

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject
from deta import Base  # type: ignore


class LoggingMiddleware(BaseMiddleware):
    """
    Middleware for logging updates.
    """

    def __init__(self, expire_after: Optional[int] = None) -> None:
        super().__init__()
        self.expire_after = expire_after

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
            expire_in=self.expire_after
        )

        return await handler(event, data)
