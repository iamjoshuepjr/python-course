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