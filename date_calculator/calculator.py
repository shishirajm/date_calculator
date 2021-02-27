from date import Date


def get_dates_diff(date1, date2):
    try:
        print(date1)
        print(date2)
        d1 = Date(date1)
        d2 = Date(date2)
        print(d1.day, d1.month, d1.year)
        print(d2.day, d2.month, d2.year)
    except Exception as e:
        print(e)
    return 0
