import argparse


def validate_str(value: str = "") -> str:
    cleaned_str = value.strip()

    if not cleaned_str:
        msg = "Empty value"
        raise argparse.ArgumentTypeError(msg)

    return cleaned_str


def validate_positive_int(value: str = "") -> int:
    try:
        number = int(value)
    except ValueError as e:
        msg = "Invalid integer value"
        raise argparse.ArgumentTypeError(msg) from e

    if number <= 0:
        msg = "Value should be a positive number"
        raise argparse.ArgumentTypeError(msg)
    return number
