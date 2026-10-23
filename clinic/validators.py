
"""Pure validation and cleaning functions for raw patient data."""


class InvalidRecordError(Exception):
    """Raised when a patient row cannot be repaired safely."""


def clean_name(raw_name: str) -> str:
    """Clean a patient name and convert it to Title Case."""
    name = raw_name.strip().title()

    if not name:
        raise InvalidRecordError("name is missing")

    return name


def parse_age(raw_age: str) -> int:
    """Convert age text to an integer between 1 and 120."""
    try:
        age = int(raw_age.strip())
    except (ValueError, AttributeError):
        raise InvalidRecordError("age must be a number") from None

    if not 1 <= age <= 120:
        raise InvalidRecordError("age must be between 1 and 120")

    return age


def parse_fee(raw_fee: str) -> float:
    """Convert a fee such as '1,250.50' to a non-negative float."""
    try:
        fee = float(raw_fee.replace(",", "").strip())
    except (ValueError, AttributeError):
        raise InvalidRecordError("fee must be a number") from None

    if fee < 0:
        raise InvalidRecordError("fee cannot be negative")

    return fee


def clean_department(raw_dept: str, default: str = "General") -> str:
    """Clean the department name or use the default."""
    department = raw_dept.strip().title()
    return department if department else default
