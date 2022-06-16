import datetime

x = datetime.date(2022, 3, 8)

delta = datetime.timedelta(days=1)

# print(x.__rsub__(y).days * 24 * 60)
print(x.weekday() == 1)
print(x.day)
