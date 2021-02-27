months30 = [4, 6, 9, 11]
days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


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


def is_valid_date(day, month, year):
    if check_month(month) and check_day(day, month, year) and check_year(year):
        return True

    return False


def count_leap_years(year):
    return int(year / 4) - int(year / 100) + int(year / 400)


def number_of_days_since_beginning_of_date(day, month, year):
    consider_year = year - 1
    year_days = consider_year * 365
    leap_days = count_leap_years(consider_year)

    if month > 2 and is_leap_year(year):
        leap_days += 1

    month_days = 0
    for index in range(month - 1):
        month_days += days_by_month[index]

    return year_days + leap_days + month_days + day - 1

