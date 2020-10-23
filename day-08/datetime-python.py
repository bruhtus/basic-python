from datetime import datetime

now = datetime.now()
print(now)

print(f'day: {now.day}')
print(f'month: {now.month}')
print(f'year: {now.year}\n')

print(f'hour: {now.hour}')
print(f'minute: {now.minute}')
print(f'second: {now.second}\n')

print(f'timestamp: {now.timestamp()}\n') #unix timestamp is the number of seconds elapsed from 1st of january 1970 UTC.

new_year = datetime(2020, 1, 1)
print(new_year)

print(f'day: {new_year.day}')
print(f'month: {new_year.month}')
print(f'year: {new_year.year}')

print(f'hour: {new_year.hour}')
print(f'minute: {new_year.minute}')
print(f'second: {new_year.second}')
