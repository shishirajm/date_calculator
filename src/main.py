from src.calculator import get_dates_diff
from src.handle_io import get_dates, show_date_difference, show_error


def main():
    date1, date2 = get_dates()
    difference, msg = get_dates_diff(date1, date2)
    if difference >= 0:
        show_date_difference(date1, date2, difference)
    else:
        show_error(date1, date2, msg)


if __name__ == '__main__':
    main()
