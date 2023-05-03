# ===============================================================
#                Get current date and time
# ===============================================================
# There are multiple ways to get the current date and time 
# in Python, using the built-in and third-party modules. 

# ===================
#  current datatime
# ===================
from datetime import datetime

now = datetime.now()
print(f'\nCurrent datetime: {now}\nType: {type(now)}')

# ==========================================================
#  extract current data and time separately from a datetime
# ==========================================================
current_date = now.date()
print(f'* Date: {current_date}\n - Type: {type(current_date)}')

current_time = now.time()
print(f'* Time: {current_time}\n - Type: {type(current_time)}')

# =====================================================================
#  break datatime to get current year, month, day hour, minute, second
# =====================================================================
print(f'+-------------------+\
      \n Year: {now.year}\
      \n Month: {now.month}\
      \n Day: {now.day}\
      \n+-------------------+\
      \n Hour: {now.hour}\
      \n Minute: {now.minute}\
      \n Second: {now.second}\
      \n Microsecond: {now.microsecond}\
      \n+-------------------+')
