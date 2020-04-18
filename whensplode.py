
import datetime
import sys
from calendar import monthrange


def datef(date):
    return date.strftime("%Y-%m-%d")


def days_until(date_target):
    date_current = datetime.datetime.now()
    return (date_target - date_current).days + 1


def announce_days_until(date_target, message):
    days = days_until(date_target)

    if days < -1:
        announcement = f"{datef(date_target)} was {abs(days)} days ago"
    elif days == -1:
        announcement = f"{datef(date_target)} was yesterday"
    elif days == 0:
        announcement = f"{datef(date_target)} is today"
    elif days == 1:
        announcement = f"There's one day until {datef(date_target)}"
    elif days > 1:
        announcement = f"There are {days} days until {datef(date_target)}"

    if message:
        announcement += f", {message}"
    else:
        announcement += "."

    print(announcement)


def int_input(prompt, min, max):
    try:
        user_input = int(input(prompt))
        if user_input < min:
            print(f"Error: Input below minimum value. Enter a number {min} or higher.")
            return int_input(prompt)
        if user_input > max:
            print(f"Error: Input above maximum value. Enter a number {max} or lower.")
            return int_input(prompt)
        return user_input
    except:
        print("Error: Expected an integer. Enter a valid number.")
        return int_input(prompt)


def get_user_date():
    year = int_input(
        "Year (YYYY): ", 1970, 3000)
    month = int_input(
        " Month (MM): ", 1, 12)
    day = int_input(
        "   Day (DD): ", 1, monthrange(year, month)[1])

    return datetime.datetime(year, month, day)


###


date_shona_30 = datetime.datetime(2026, 11, 12)  # Shona's 30th birthday
announce_days_until(date_shona_30, "Shona's 30th birthday, when she will explode.")

while True:
    response = input("Check days until a different date? (y/n): ")
    if response == "y":
        # TODO function to select random message for announcements
        announce_days_until(get_user_date(), None)
    elif response == "n":
        sys.exit(0)
