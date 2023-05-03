# ===============================================================
#                Get current date and time
# ===============================================================
# There are multiple ways to get the current date and time 
# in Python, using the built-in and third-party modules. 

# ===================
#  current datatime
# ===================
from datetime import datetime, timezone, date 
import time

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
      \n Seconds: {now.second}\
      \n Microseconds: {now.microsecond}\
      \n+-------------------+') 

# =========================================
#  get current date using the date class
# =========================================
today = date.today()
print(f'\n+------------------------------------+\
        \n* Current date: {today}')

# ==============================================
#  get current time in seconds with time class
# ==============================================
seconds = time.time()
print(f'* Time in seconds {seconds}')        

# =========================================
#  get current date using the time.ctime()
# =========================================
print(f'* Current Time: {time.ctime(time.time())}')

# =============================================
#  get current date using the time.localtime()
# =============================================
local = time.localtime(time.time())

print(f'+-------------------+\
      \n Year: {local.tm_year}\
      \n Month: {local.tm_mon}\
      \n Day: {local.tm_mday}\
      \n+-------------------+\
      \n Hour: {local.tm_hour}\
      \n Minute: {local.tm_min}\
      \n Seconds: {local.tm_sec}\
      \n+-------------------+') 

# ====================================
#  get current time in milliseconds
# ====================================
miliseconds = time.time()
miliseconds = int(miliseconds * 1000)
print(f'Miliseconds: {miliseconds}')

# =============================================
#  get current Coordinate Universal Time (UTC) 
# =============================================
now = datetime.now(timezone.utc)
print(f'Current UTC Time: {now}')

# ===========================================
#  get current Greenwich Mean Time (GMT) 
# ===========================================
gmt = time.gmtime(time.time())
print(f'GMT Time: {gmt}')
print(f'{gmt.tm_hour}: {gmt.tm_min}: {gmt.tm_sec}')

# ===================================
#  get current time in ISO format 
# ===================================
dt_iso = datetime.now().isoformat()
print(f'Current DateTime in ISO: {dt_iso}')
