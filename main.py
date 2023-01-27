import re


def is_date_format_correct(date: str) -> bool:
    """
    This function takes in a date in string format
    and returns true if the date matches the format
    YYYY-MM-DD and false if it doesn't
    """

    correct_format = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(correct_format.match(date))


print(is_date_format_correct("1999-01-01"))
print(is_date_format_correct("1999/01/01"))
