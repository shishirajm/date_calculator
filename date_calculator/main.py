import calculator, handleIO


def main():
    date1, date2 = handleIO.get_dates()
    difference = calculator.get_dates_diff(date1, date2)
    handleIO.show_date_difference(date1, date2, difference)


if __name__ == '__main__':
    main()
