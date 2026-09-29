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


def validate_date(value: str) -> str | None:
    try:
        date.fromisoformat(value)
        return value
    except ValueError:
        return None


def validate_time(value: str) -> str | None:
    try:
        time.fromisoformat(value)
        return value
    except ValueError:
        return None


def validate_datetime(value: str) -> str | None:
    try:
        datetime.fromisoformat(value)
        return value
    except ValueError:
        return None
