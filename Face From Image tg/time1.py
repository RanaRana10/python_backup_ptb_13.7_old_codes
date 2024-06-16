# import pytz
# kolkata_tz=pytz.timezone('Asia/Kolkata')

# from datetime import datetime
# kolkata_time = datetime.now(kolkata_tz)
# formatted_time = kolkata_time.strftime('%Y-%m-%d %H:%M:%S %Z')
# print(f"Current time in Kolkata: {formatted_time}")


# import pytz

# List all available time zones
# all_timezones = pytz.all_timezones
# for timezone in all_timezones:
# print(all_timezones)


import pytz

# List commonly used time zones
common_timezones = pytz.common_timezones
for timezone in common_timezones:
    print(timezone)
