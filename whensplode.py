#!/usr/bin/env python
# do chmod 744 FILENAME.extension
# run with "./FILENAME.extension"
# or just "py whensplode.py"

import datetime


def datef(date):
    return date.strftime("%Y-%m-%d")


def days_until(date_target):
    date_current = datetime.datetime.now()
    return (date_target - date_current).days


def announce_days_until(date_target, message):
    print(f"There are {days_until(date_target)} "
          f"days until {datef(date_target)}, "
          f"{message}")


date_shona_30 = datetime.datetime(2026, 11, 12)  # Shona's 30th birthday
announce_days_until(date_shona_30, "Shona's 30th birthday, when she will explode.")
