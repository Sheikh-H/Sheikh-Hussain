import re
from datetime import date, datetime, time

invalid_characters = {"|", "^", "$", "{", "}"}
date_pattern = r"^\d{4}-\d{2}-\d{2}$"
date_pattern = r"^\d{4}-\d{2}-\d{2}$"
time_pattern = r"^\d{2}:\d{2}:\d{2}$"
datetime_pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$"


def validate_username(value: str) -> str | None:
    for char in value:
        if char in invalid_characters:
            return None
    if len(value) > 255:
        return None
    return value


def validate_password(value: str) -> str | None:
    for char in value:
        if char in invalid_characters:
            return None
    if len(value) > 255:
        return None
    if len(value) < 10:
        return None
    return value


def validate_input(value: str) -> str | None:
    if not value:
        return None
    for char in value:
        if char in invalid_characters:
            return None
    return value


def validate_date(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def validate_time(value: str) -> time | None:
    try:
        return time.fromisoformat(value)
    except ValueError:
        return None


def validate_datetime(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def validate_integer(value: int | str) -> int | None:
    if value.isdigit():
        return int(value)
    if isinstance(value, int):
        return value
    return None
