from datetime import date

d = date(2020, 1, 1)
print(f'{d}\n')

today = date.today()
print(f'current date: {today}\n')

print(f'current year: {today.year}')
print(f'current month: {today.month}')
print(f'current day: {today.day}')
