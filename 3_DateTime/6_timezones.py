# ==========================
#  Working with Timezones 
# ==========================
from datetime import datetime, timedelta, timezone
import pytz 

# current DateTime
unaware = datetime.now()
print(f'Timezone naive: {unaware}')

# Standard UTC timezone aware Datetime
aware = datetime.now(pytz.utc)
print(f'Timezone Aware: {aware}')

# US/Cetral timezone datetime
aware_us_central = datetime.now(pytz.timezone('US/Central'))
print(f'US Central Date: {aware_us_central}')

unaware = datetime(2023, 5, 4, 11, 28, 5)
print(f'Timezone naive: {unaware}')

aware = unaware.replace(tzinfo=pytz.UTC)
print(aware)

# =============================================
# Format UTC DateTime to get the timezone name
# =============================================

datetime_india = datetime.now(pytz.timezone('Asia/Kolkata'))
print(f'Formatted DateTime in IST: {datetime_india.strftime("%Y/%m/%d %H:%M:%S")}')

# ===========================================================
# Create Timezone aware Datetime object using timezone class
# ===========================================================
# naive
naive = datetime.now()
print(f'Naive DateTime: {naive}')

# UTC aware
UTC = datetime.now(timezone.utc)
print(f'UTC DateTime: {UTC}')

# creating a datetime with JST (Japan) TimeZone
jst_dateTime = datetime.now(timezone(timedelta(hours =+ 9), 'JST'))
print(f'In JST: {jst_dateTime}')

# =========================================
#  Get current time in different timezone 
# =========================================
dt_us_central = datetime.now(pytz.timezone('America/Mexico_City'))
print(f'US Central timezone DateTime: {dt_us_central.strftime("%Y/%m/%d %H:%M:%S: %Z %z")}')

dt_us_pacific = datetime.now(pytz.timezone('America/Tijuana'))
print(f'US Pacific timezone DateTime: {dt_us_pacific.strftime("%Y/%m/%d %H:%M:%S: %Z %z")}')

dt_us_eastern =  datetime.now(pytz.timezone('America/New_York'))
print(f'US Eastern timezone DateTime: {dt_us_eastern.strftime("%Y/%m/%d %H:%M:%S: %Z %z")}')

dt_us_mountain = datetime.now(pytz.timezone('America/Chihuahua'))
print(f'US Mountain timezone DateTime: {dt_us_mountain.strftime("%Y/%m/%d %H:%M:%S: %Z %z")}')

dt_japan = datetime.now(pytz.timezone('Asia/Tokyo'))
print(f'Japan DateTime: {dt_japan.strftime("%Y/%m/%d %H:%M:%S: %Z %z")}')

dt_brazil = datetime.now(pytz.timezone('America/Sao_Paulo'))
print(f'Brazil DateTime: {dt_brazil.strftime("%Y/%m/%d %H:%M:%S: %Z %z")}')

dt_uk = datetime.now(pytz.timezone(f'Europe/London'))
print(f'UK DateTime: {dt_uk.strftime("%Y/%m/%d %H:%M:%S: %Z %z")}')

# =======================================
#  Get timezone information using tzinfo
# =======================================
print(f'TimeZone Name: {dt_us_eastern.tzname()}')
print(f'UTC Offset: {dt_us_eastern.utcoffset()}')
print(f'DST: {dt_us_eastern.dst()}')

# ==============================
#  Converting Between Timezones
# ==============================

# UTC timezone DateTime
dt_local = datetime.now(pytz.utc)
print(f'UTC DateTime: {dt_local.strftime("%Y/%m/%d %H:%M:%S %Z %z")}')

# convert UTC timezone to 'US/Central'
dt_us_central = dt_local.astimezone(pytz.timezone('US/Central'))
print(f'US Central DateTime: {dt_us_central.strftime("%Y/%m/%d %H:%M:%S %Z %z")}')

# convert 'US/Central' timezone to US/Eastern
dt_us_eastern = dt_us_central.astimezone(pytz.timezone('America/New_York'))
print(f'US Eastern DateTime: {dt_us_eastern.strftime("%Y/%m/%d %H:%M:%S %Z %z")}')

# convert 'US/Eastern' timezone to CST (Colombia)
dt_col = dt_us_central.astimezone(pytz.timezone('America/Bogota'))
print(f'Colombia DateTime: {dt_col.strftime("%Y/%m/%d %H:%M:%S %Z %z")}')

# ==============================
#  Working with local Timezones
# ==============================

fmt = '%Y-%m-%d %H:%M:%S %Z %z'
tz_colombia = pytz.timezone('America/Bogota')
ist_local = tz_colombia.localize(datetime.now())
print(f'Colombian Standard Time: {ist_local.strftime(fmt)}')

amdam_tz = pytz.timezone('Europe/Amsterdam')
dt = datetime(1999, 1, 24, 11, 30, 24)
cest_local = amdam_tz.localize(dt, is_dst=True)
print(f'Amsterdam with dayligth saving time: {cest_local.strftime(fmt)}')

print(f'Daylight saving time in Amsterdam on 24/01/1999: {cest_local.tzinfo.dst(cest_local)}')
