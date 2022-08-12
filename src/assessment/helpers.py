import datetime

from dateutil.relativedelta import relativedelta


def calculate_dob(dob: datetime.date) -> int:
    """Calculate a person's age given a valid datetime date"""
    now = datetime.date.today()
    r_delta = relativedelta(now, dob)
    return int(r_delta.years)
