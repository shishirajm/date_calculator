# import date_formatter
# import date_utils
from my_calculator import date_formatter, date_utils


class Date(object):
    def __init__(self, date, format=None):
        extractor = date_formatter.FormatterFactory()
        day, month, year = extractor.extract(date, format)
        if date_utils.is_valid_date(day, month, year):
            self._day = day
            self._month = month
            self._year = year

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    def __sub__(self, other):
        days = date_utils.number_of_days_since_beginning_of_date(self.day, self.month, self.year)
        days2 = date_utils.number_of_days_since_beginning_of_date(other.day, other.month, other.year)
        day_difference = abs(days2 - days)
        days_elapsed = 0 if day_difference == 0 else day_difference - 1
        return days_elapsed
