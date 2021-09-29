from datetime import date
from datetime import datetime


def date_to_string(date: date) -> str:
    """
    function that expect some date and return the data in string format.

    :param date: date

    :return string 
    """

    return date.strftime("%d/%m/%y")


def string_to_date(date: str) -> date:
    """
    function that expect some date in string and return the data in datetime format.

    :param date: string

    :return datetime 
    """
    return datetime.strptime(date, "%d/%m/%y")


def format_float_to_str_moeda(value: float) -> str:
    """
    function that expect some value and return the value in string format.

    :param value: float

    :return string 
    """
    return f'R$ {value:,.2f}'
