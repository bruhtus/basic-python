from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20) #week converted to 7 days, hour converted to 3600 seconds, a minute converted to 60 seconds, a millisecond converted to 1000 microseconds.
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2

print(f't3 = {t3}')
