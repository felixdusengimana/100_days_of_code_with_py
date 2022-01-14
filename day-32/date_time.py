import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
print(year)
day = now.day
print(day)
month = now.month
print(month)
week_day = now.weekday()
print(week_day)

date_of_birth = dt.datetime(year=1, month=11, day=5)
print(date_of_birth)