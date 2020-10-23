from datetime import time

a = time()
print(f'time(hour=0, minute=0, second=0) = {a}')

b = time(10, 30, 50)
print(f'time(hour=10, minute=30, second=50) = {b}')

c = time(10, 30, 50, 200555)
print(f'time(hour=10, minute=30, second=50, microsecond=200555) = {c}')
