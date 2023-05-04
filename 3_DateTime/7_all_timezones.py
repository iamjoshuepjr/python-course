# ==================================
# Get list of all timezones name
# ==================================

import pytz 
print(f'\n+----------------------------------+\
        \n             Timezones\
        \n+----------------------------------+')
for timezone in pytz.all_timezones:
    print(timezone)

print(f'\n+----------------------------------+\
        \n            Timezones Set\
        \n+----------------------------------+')
for timezone in pytz.all_timezones_set:
    print(timezone)

# =======================
# Get common TimeZones 
# =======================

print(f'\n+----------------------------------+\
        \n    Most commonly used timezones\
        \n+----------------------------------+')

for timezone in pytz.common_timezones:
    print(timezone)

print(f'\n+------------+\
        \n  lenght: {len(pytz.common_timezones)}\
        \n+------------+')

# ============================
# Get TimeZones of any coutry
# ============================
print(f'\n+----------------------------------+\
        \n            US timezones\
        \n+----------------------------------+')
for timezone in pytz.country_timezones['US']:
    print(timezone)

# ============================
# Get TimeZones of coutry
# ============================

print(f'\n+----------------------------------+\
        \n      Country Names with code\
        \n+----------------------------------+')
for code, name in pytz.country_names.items():
    print(f'Code {code} : Name {name}')

print(f'\n+----------------------------------+\
        \n * Country full name {pytz.country_names["US"]}\
        \n+----------------------------------+')



