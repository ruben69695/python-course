# ================== Datetime module ===============
print("\n================== Datetime module ===============\n")

import datetime

dt = datetime.datetime.now()
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

print("{}/{}/{}".format(dt.day, dt.month, dt.year))
print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))

dt = datetime.datetime(2000, 12, 21, 4, 50, 45)
print(dt)
dt = dt.replace(year=2018)
print(dt)

dt = datetime.datetime.now()
print(dt.isoformat())

print(dt.strftime("%A %d %B %Y %I:%M"))

import locale

locale.setlocale(locale.LC_ALL, '')
print(dt.strftime("%A %d %B %Y %I:%M"))

print(dt.strftime("%A %d de %B del %Y - %H:%M"))

dt = datetime.datetime.now()
t = datetime.timedelta(days=3, hours=2, seconds=20)

in_three_days = dt + t
print(in_three_days.strftime("%A %d de %B del %Y - %H:%M"))

three_days_back = dt - t
print(three_days_back.strftime("%A %d de %B del %Y - %H:%M"))

import pytz
#print(pytz.all_timezones)
dt = datetime.datetime.now(pytz.timezone('US/Hawaii'))
print(dt.strftime("%A %d de %B del %Y - %H:%M"))