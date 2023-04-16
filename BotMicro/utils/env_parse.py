from typing import Optional


def parse_expire_after(expire_after_str: str) -> Optional[int]:
    try:
        return int(expire_after_str)
    except ValueError:
        return None
