
import datetime
import sys


def datef(date):
    return date.strftime("%Y-%m-%d")


def days_until(date_target):
    date_current = datetime.datetime.now()
    return (date_target - date_current).days


def announce_days_until(date_target, message):
    print(f"There are {days_until(date_target)} "
          f"days until {datef(date_target)}, "
          f"{message}")


def get_user_date():
    year = int(input(
        "Year (YYYY): "))
    month = int(input(
        " Month (MM): "))
    day = int(input(
        "   Day (DD): "))
    user_date = datetime.datetime(year, month, day)
    announce_days_until(user_date, None)


date_shona_30 = datetime.datetime(2026, 11, 12)  # Shona's 30th birthday
announce_days_until(date_shona_30, "Shona's 30th birthday, when she will explode.")

while True:
    response = input("Check days until a different date? (y/n): ")
    if response == "y":
        get_user_date()
    elif response == "n":
        sys.exit(0)
