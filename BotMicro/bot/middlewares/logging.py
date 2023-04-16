from typing import Any, Awaitable, Callable, Dict, Optional

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import TelegramObject

from utils.logging import log_to_deta  # type: ignore


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
        await log_to_deta(
            data={'update': event.json()},
            expire_after=self.expire_after
        )
        return await handler(event, data)
