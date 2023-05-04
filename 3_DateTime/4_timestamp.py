# =======================
#  Get current Timestamp
# =======================
from datetime import datetime, timezone
date_time = datetime.now()

time_stamp = datetime.timestamp(date_time)
print(f'Date and time is: {date_time}\
    \nTimestamp (datetime module): {time_stamp}')

# =================================
#  Get Timestamp using time module
# =================================
import time 
get_stamp = time.time()
print(f'Timestamp (time module): {get_stamp}')

# ======================================
#  Get Timestamp using calendar module
# ======================================
import calendar
current_GMT = time.gmtime()
ts = calendar.timegm(current_GMT)
print(f'Current timestap (calendar module) {ts}')

# =================================
#  convert Timestamp to datetime 
# =================================
dt = datetime.fromtimestamp(ts)
print(f'Date and Time: {dt}')

# ===============================
#  convert Timestamp to String
# ===============================
# convert to datetime
to_datetime = datetime.fromtimestamp(ts)
# convert to string
date_time_str = to_datetime.strftime("%d-%m-%Y, %H:%M:%S")
print(f'Full datetime: {date_time_str}')

date_str = to_datetime.strftime("%d-%B, %Y") 
print(f'Date: {date_str}')

time_str = to_datetime.strftime("%I:%M:%S %p")
print(f'Time: {time_str}')

# ===============================
#  get Timestamp in milliseconds
# ===============================
# date in string format 
birthday = "24/01/1999 11:30:24"

# convert to datetime instance
date_time = datetime.strptime(birthday, '%d/%m/%Y %H:%M:%S')

# timestamp in millisenconds
ts = date_time.timestamp() * 1000
print(f'Birthday to Milliseconds: {ts}')

# ==========================
#  get the UTC Timestamp 
# ==========================

utc_timestamp = date_time.replace(tzinfo=timezone.utc).timestamp()
print(f'Birthday to UTC: {utc_timestamp}')

# =====================================
#  Timestamp with a different Timezone
# =====================================
# timezone name
date_string = "03/May/2023:19:04:10 UTC +0900"
dt_format = datetime.strptime(date_string, '%d/%b/%Y:%H:%M:%S %Z %z')
print(f'Date with Timezone name: {dt_format}')

# timestamp
timestamp = dt_format.timestamp()
print(f'Timestamp is: {timestamp}')

# =========================================
# Convert an integer Timestamp to datetime
# =========================================
date = datetime.utcfromtimestamp(timestamp/1e3)
print(f'Corresponding date for the integer timestamp {timestamp}: {date}')