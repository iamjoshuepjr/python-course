# =========================================================================
#            Convert an integer Timestamp to datetime
# =========================================================================
# A timedelta represents a duration whicj is the difference between 
# two dates, time, or datetimes instances, to the microseconds resolution.

from datetime import datetime, timedelta
# given datetime
current_date = datetime.now()
x_datetime = datetime(year=2023, month=1, day=24, hour=19, minute=27)

# difference between two dates
# get timedelta
delta = current_date - x_datetime

print(f'Timedelta: {delta}')
print(f'Timedelta Type: {type(delta)}')

# ============================
# Calculate future datetime
# ============================
print('Given Date:', current_date)

# add 4 weeks in given date
new_date = current_date + timedelta(weeks=4)
print('Future Date:', new_date)

# =========================================
#            TimeDelta object
# =========================================
# The timedelta object has seven arguments:
# Days, seconds, minutes, hours, weeks, 
# milliseconds, and microseconds. 
# All seven arguments are optional, and the
# default value is 0. 
# (They can be either integers or float)

sample_timedelta = timedelta(
    days = 99,
    seconds = 4,
    microseconds = 2,
    milliseconds = 1200,
    minutes = 3,
    hours = 23,
    weeks = 23
)

# all values will be changed to seconds, microseconds and days
print(sample_timedelta)
print(type(sample_timedelta))

# =========================================
#            TimeDelta attributes
# =========================================
timedelta1 = datetime(year = 2023, month = 5, day =  4, hour = 9, minute = 10)
timedelta2 = datetime(year = 2023, month = 5, day =  5, hour = 9, minute = 10)

# get timedelta by substracting two dates
final = timedelta2 - timedelta1
# get timedelta attributes
print(f'Days: {final.days}\
      \nMicroseconds: {final.microseconds}\
      \nSeconds: {final.seconds}\
      \nMax: {final.max}\
      \nMin: {final.min}\
      \nResolution: {final.resolution}\
      \nTotal Seconds: {final.total_seconds()}')

# =========================================
#            TimeDelta with weeks
# =========================================
today = datetime.now()
print(f'Current Date and Time: {today}')

# substracting 6 weeks
past_date = today - timedelta(weeks = 6)
print(f'Past Date: {past_date}')

# adding 2 weeks
future_date = today + timedelta(weeks = 2)
print(f'Future Date: {future_date}')

# ================================================
#     TimeDelta with seconds and microseconds
# ================================================
future_date = today + timedelta(seconds = 60)
print(f'60 seconds After: {future_date}')

# substract 500 milliseconds
past_date = today - timedelta(milliseconds = 500)
print(f'500 Milliseconds Before: {past_date}')

# =============================
#     TimeDelta to seconds
# =============================
minutes = timedelta(minutes = 20)
print(f'Seconds in {minutes}: {minutes.total_seconds()}')

# =============================
#     TimeDelta with days
# =============================
future_date = today +  timedelta(days = 100)
print(f'Date 100 days later: {future_date}')

past_date = today - timedelta(days = 100)
print(f'Date 100 days Before: {past_date}')

# =============================
#     TimeDelta with hours
# =============================
future_date = today + timedelta(hours = 12)
print(f'Date 12 hours later: {future_date}')

past_date = today - timedelta(hours = 6)
print(f'Date 6 hours before: {past_date}')

# =========================================
#  Add or Substract two Timedelta objects
# =========================================

# create timedelta 
timedelta1 = timedelta(weeks = 2, days = 2)
timedelta2 = timedelta(hours = 12, minutes = 30)

# add two timedelta
final = timedelta1 + timedelta2

# add timedelta to current date
future_date =  today + final 
print(f'Future report date: {future_date}')

# substract two timedelta
final = timedelta1 - timedelta2

# substract timedelta to current date
past_date = today - final
print(f'Past report date: {past_date}')

# ==========================
#  Formating a Timedelta 
# ==========================
print(f'Current Date (str): {str(today)}')

# add timedelta to date
month_later = today +  timedelta(days = 20)

print(f'Formatted DateTime: {month_later.strftime("%Y/%m/%d %H:%M:%S %p")}')

# ==========================
#  String to Timedelta 
# ==========================
dt_string = '04/05/2023 9:44:00'
date = datetime.strptime(dt_string, '%d/%m/%Y %H:%M:%S')
print(f'Given date is: {date}')

# extracting timedelta information from this date
tdelta = timedelta(hours = date.hour, minutes = date.minute, seconds = date.second)
print(f'Timedelta: {tdelta}')