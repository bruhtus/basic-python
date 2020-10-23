from datetime import datetime

date_string = '23 Oct, 2020'
print(f'date in string: {date_string}')

date_object = datetime.strptime(date_string, '%d %b, %Y')
print(f'from string to time: {date_object}')
