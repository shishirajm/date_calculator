months30 = [4, 6, 9, 11]


def check_month(month):
    if month < 1 or month > 12:
        raise Exception(f'"{month}" is invalid month')
    return True


def is_leap_year(year):
    if year % 4 != 0:
        return False

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return True


def check_day(day, month, year):
    if day < 1 or day > 31:
        raise Exception(f'"{day}" is invalid day')

    if day == 31 and month in months30:
        raise Exception(f'"{day}" is invalid day for month {month}')

    if month == 2 and day > 29:
        raise Exception(f'"{day}" is invalid day for month {month}')
    elif day == 29 and not is_leap_year(year):
        raise Exception(f'"{day}" is invalid day for month {month} and year {year}')
    
    return True


def check_year(year):
    if year < 1:
        raise Exception(f'"{year}" is invalid year')

    return True


class Date(object):
    default_format = "DD/MM/YYYY"

    def __init__(self, date, format=None):
        self._format = self.default_format if format is None else format
        if self._format == self.default_format:
            day, month, year = self.get_day_month_year_default(date)
            if check_month(month) and check_day(day, month, year) and check_year(year):
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

    def get_day_month_year_default(self, date):
        if self._format is not self.default_format:
            raise Exception(f'"{date}" is in unsupported format, use format "{self.default_format}"')
        
        if date.count('/') != 2:
            raise Exception(f'"{date}" is in unsupported format, use format "{self.default_format}"')

        try:
            return list(map(lambda x: int(x), date.split('/')))
        except Exception as e:
            raise Exception(f'"{date}" is in unsupported format, use format "{self.default_format}"')
