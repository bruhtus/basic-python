from datetime import date
from datetime import datetime

today = date.today()
new_year = date(year=2021, month=1, day=1)

day_left_for_newyear = new_year - today
print(f'day left for new year: {day_left_for_newyear}\n')

now = datetime.now()

today_with_time = datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
new_year_datetime = datetime(year=2021, month=1, day=1)

time_left_newyear = new_year_datetime - today_with_time
print(f'day left for new year with time: {time_left_newyear}')
