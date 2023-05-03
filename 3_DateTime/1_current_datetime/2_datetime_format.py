# ====================================================================== 
#                  DateTime Format (Strftime)
# ====================================================================== 
# In Python, the date and time values are stored as datetime objects, 
# but there are cases where we need to print the datetime objects into 
# various string formats for better readability.
# For example, you may need to represent a date numerically in format, 
# like “17-06-2021“. On the other hand, you want to convert dates in 
# textual string format like “Tuesday, 23 June 2021.”

from datetime import datetime 

# current datetime
now = datetime.now()

# convert to string
date_time = now.strftime('%Y-%m-%d-%H:%M:%S')
print(f'DateTime String: {date_time}')

# ======================================================================
# Convert individual attribuyes of a datetime object to a string format
# ======================================================================

date = now.strftime('%Y-%m-%d')
print(f'Date String: {date}')

time = now.strftime('%H:%M:%S')
print(f'Time String: {time}')

year = now.strftime('%Y')
print(f'Year String: {year}')

month = now.strftime('%m')
print(f'Month String: {month}')

day = now.strftime('%d')
print(f'Day String: {day}')

# ====================================
#  Represent Dates in Textual Format 
# ====================================
# Full Textual Mode
print(f'dd-MonthName-yyyy: {now.strftime("%d-%B-%Y")}')
print(f'DayName-MonthName-yyyy: {now.strftime("%A, %d - %B, %Y")}')

# Short Textual Mode
print(f'dd-MonthName-yyyy: {now.strftime("%d-%b-%Y")}')
print(f'DDD-dd-MMM-yyyy: {now.strftime("%a, %d - %b, %Y")}')

# ====================================
#  Convert only date to string 
# ====================================
from datetime import date 
# current date
today = date.today()
print("Today's date:", today)

# format date
print('Date String', today.strftime("%d-%m-%y"))

to_day = datetime.now().date()
# format date
print('Date String', to_day.strftime("%d-%m-%y"))

# ==================================================
#  Represent time in 24-hours and 12-hours format
# ==================================================
dateformat = datetime.now().time()
print(f'Current Time: {dateformat}')

print(f'Time in 24 hours format: {dateformat.strftime("%H-%M-%S")}')
print(f'Time in 12 hours format: {dateformat.strftime("%I-%M-%S")}')

# =========================================
#  Represent time in microseconds format
# =========================================
print(f'Time in Microseconds: {dateformat.strftime("%H:%M:%S.%f")}')

# =========================================
#  Represent time in AM/PM format
# =========================================
ampm = datetime.now()
print(f'Current Time: {ampm}')

print(f'Time is: {ampm.strftime("%d-%b-%Y %I:%M %p")}')
print(f'Time is: {ampm.strftime("%H:%M %p")}')

import time

time_obj = time.time()
local_time = time.localtime(time_obj)
print(f'Time Tuple: {local_time}')

print(f'Formatted Time: {time.strftime("%d/%m/%y %H:%M:%S", local_time)}')

# =======================================
#  Convert Datetime to locale's format
# =======================================
local = datetime.now()
print(f'Date is: {local}')
print(f'Date is: {local.strftime("%c")}')

