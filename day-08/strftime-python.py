from datetime import datetime

now = datetime.now()
t = now.strftime('%H:%M:%S')
print(f'time: {t}')

print(f'format mm/dd/yy H:M:S format: {now.strftime("%m/%d/%Y, %H:%M:%S")}')
print(f'format dd/mm/yy H:M:S format: {now.strftime("%d/%m/%Y, %H:%M:%S")}')
