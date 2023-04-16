from datetime import datetime
from typing import Any, Optional

from aiogram import Router
from deta import Base

router = Router()


async def log_to_deta(
    data: dict[str, Any],
    expire_after: Optional[int] = None,
    base_name: str = 'logs'
):
    time = datetime.now()
    log_data = {'time': time.isoformat()}
    log_data.update(data)

    logging_base = Base(base_name)
    logging_base.put(
        key=str(2 * 10**9 - time.timestamp()),  # used for sorting by time
        data=log_data,
        expire_in=expire_after
    )
