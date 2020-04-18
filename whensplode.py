
import datetime
import sys


def datef(date):
    return date.strftime("%Y-%m-%d")


def days_until(date_target):
    date_current = datetime.datetime.now()
    return (date_target - date_current).days + 1


def announce_days_until(date_target, message):
    days = days_until(date_target)

    if days < -1:
        announcement = f"{datef(date_target)} was {days} days ago"
    elif days == -1:
        announcement = f"{datef(date_target)} was yesterday"
    elif days == 0:
        announcement = f"{datef(date_target)} is today"
    elif days == 1:
        announcement = f"There's one day until {datef(date_target)}"
    elif days > 1:
        announcement = f"There are {days} days until {datef(date_target)}"

    # TODO function to select random message
    if message:
        announcement += f", {message}"
    else:
        announcement += "."

    print(announcement)


def int_input(prompt):
    try:
        return int(input(prompt))
    except:
        print("Error: Expected an integer. Enter a valid number.")
        return int_input(prompt)


def get_date_part(part, future):
    date_current = datetime.datetime.now()

    if part == "year":
        date_part = int_input("Year (YYYY): ")
        if future:  # TODO refactor into future date part function
            while date_part < date_current.year:
                print(f"Error: Date must be in the future. Enter {date_current.year} or later.")
                date_part = int_input("Year (YYYY): ")

    elif part == "month":
        date_part = int_input(" Month (MM): ")
        # TODO valid month check
        if future:
            while date_part < date_current.month:
                print(f"Error: Date must be in the future. Enter {date_current.month} or later.")
                date_part = int_input(" Month (MM): ")

    elif part == "day":
        date_part = int_input("   Day (DD): ")
        # TODO valid day check
        if future:
            while date_part < date_current.day:
                print(f"Error: Date must be in the future. Enter {date_current.day} or later.")
                date_part = int_input("   Day (DD): ")

    return date_part


def get_user_date():  # TODO allow user dates in the past
    date_current = datetime.datetime.now()

    year = get_date_part("year", True)

    if year == date_current.year:
        month = get_date_part("month", True)
    else:
        month = get_date_part("month", False)

    if (year == date_current.year) and (month == date_current.month):
        day = get_date_part("day", True)
    else:
        day = get_date_part("day", False)

    return datetime.datetime(year, month, day)


###


date_shona_30 = datetime.datetime(2026, 11, 12)  # Shona's 30th birthday
announce_days_until(date_shona_30, "Shona's 30th birthday, when she will explode.")

while True:
    response = input("Check days until a different future date? (y/n): ")
    if response == "y":
        announce_days_until(get_user_date(), None)
    elif response == "n":
        sys.exit(0)
