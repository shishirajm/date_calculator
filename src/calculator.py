from src.date import Date


def get_dates_diff(date1, date2):
    try:
        log(date1)
        log(date2)
        d1 = Date(date1)
        d2 = Date(date2)
        return d1 - d2, ''
    except Exception as e:
        log(e)
        return -1, e


def log(msg):
    print(msg)
