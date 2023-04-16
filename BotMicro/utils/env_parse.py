from typing import Optional


def parse_optional_int(expire_after_str: str) -> Optional[int]:
    try:
        return int(expire_after_str)
    except ValueError:
        return None


def parse_bool(logging_enabled_str: str) -> bool:
    return logging_enabled_str.lower() in ('true', '1', 'yes', 'y')
