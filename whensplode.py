#!/usr/bin/env python
# do chmod 744 FILENAME.extension
# run with "./FILENAME.extension"
# or just "py whensplode.py"

import datetime


date_current_full = datetime.datetime.now();
date_shona_30 = datetime.datetime(2026,11,12);  # Shona's 30th birthday
date_shona_30_strf = date_shona_30.strftime("%Y-%m-%d");

days_shona_explode = (date_shona_30 - date_current_full).days;

print(f"There are {days_shona_explode} days until {date_shona_30_strf}, Shona's 30th birthday, when she will explode.");
