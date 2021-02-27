def get_dates():
    date1 = input("Enter a Date in DD/MM/YYYY format: ")
    date2 = input("Enter a Date in DD/MM/YYYY format to find the difference: ")
    return date1, date2


def show_date_difference(date1, date2, difference):
    print("Difference between the dates ", date1, "and", date2, "is", difference, "days")
