import time
import calendar

print(time.time())

print(time.localtime(time.time()))
print(time.gmtime(time.time()))

print()

cal = calendar.month(2019,2)
print(cal)


calendar.prcal(2019)
calendar.prmonth(2019,2)
