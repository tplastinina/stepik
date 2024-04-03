import datetime

(y,m,d) = [int(n) for n in input().split()]
d = datetime.date(y, m, d)
days1 = int(input())
delta = datetime.timedelta(days=days1)
now_date = d + delta

print(now_date.year, now_date.month, now_date.day)