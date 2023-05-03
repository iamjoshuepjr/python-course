# =====================================================================
#             String to DateTime strptime()
# =====================================================================
# You need to convert a numerical string like 03-05-2023
# to a date time object, or you want to convert representing dates 
# like Wednesday, 03 May, 2023 to a datetime object.
# To convert a string into a datetime object, we can use the strptime()

from datetime import datetime
import time, locale

# Date String in dd/mm/yyyy HH:MM:SS format
datetime_str = '03/05/2023 08:50:32'

# Convert string to datetime object
datetime_str = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
print(f'Datetime: {datetime_str}')


# =======================
# String to date object
# =======================

date_str = datetime.strptime("2023/05/03 09:03:32", "%Y/%m/%d %H:%M:%S").date()
print(f'Date: {date_str}')

# =======================
# String to time object
# =======================

time_str = datetime.strptime('2023/05/03 09:03:32', '%Y/%m/%d %H:%M:%S').time()
print(f'Time: {time_str}')

# ====================================
# String to time object (time module)
# ====================================

time_str = '09-48-00'
format_time = '%H-%M-%S'

time_obj = time.strptime(time_str, format_time)
print(f'Time object: {time_obj}')
print(type(time_obj))

# ===========================================
# String with day and month name to datetime
# ===========================================
# String with full day and month names
fulldatetime = "Wednesday,03 May,2023 09:56:00"

dt_obj = datetime.strptime(fulldatetime, "%A,%d %B,%Y %H:%M:%S")
print(f'Date object: {dt_obj}')

# String with abbreviated day and month names
shortdate = "Wed, 03 May, 23"

short_dt_obj = datetime.strptime(shortdate, '%a, %d %b, %y').date()
print(f'Date object: {short_dt_obj}')

# ======================================
# Parse String with AM/PM to datetime
# ======================================

# string with a.m., p.m.
datetime_string = "03-May-2023 12:53 PM"

date_obj = datetime.strptime(datetime_string, "%d-%b-%Y %I:%M %p")
print(f"DateTime object: {date_obj}")

# ======================================
# Parse String with Timezone to datetime
# ======================================

# Date string with UTC offset
timezone = "03/May/2023:01:04:34 +0200"
tz_obj = datetime.strptime(timezone, "%d/%b/%Y:%H:%M:%S %z")
print(f'Date object with UTC offset: {tz_obj}')

# Date string with Timezone name
timezone = "03/May/2023:01:04:34 +0900"
tz_obj = datetime.strptime(timezone, "%d/%b/%Y:%H:%M:%S %z")
print(f'Date object with UTC offset: {tz_obj}')

# ===================================
#       Parse String to TimeStamp
# ====================================
birthday = "24/01/1999 11::30::24"

timeStamp = datetime.strptime(birthday, "%d/%m/%Y %H::%M::%S").timestamp()
print(f"TimeStamp: {timeStamp}")
