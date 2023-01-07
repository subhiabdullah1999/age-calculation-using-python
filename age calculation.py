
import datetime

print("*" * 60)

perthyear = int(input("please input  pertheyear : ").strip())
perthmonth = int(input("please input  perthmonth : ").strip())
perthday = int(input("please input  perthday : ").strip())

perthhour = int(input("please input  prethhour : ").strip())
perthsecond = int(input("please input  prethsecond : ").strip())

perthyearnow = datetime.datetime.now().year
perthmonthnow = datetime.datetime.now().month
perthdaynw = datetime.datetime.now().day
perthhournow = datetime.datetime.now().hour
perthsecondnow = datetime.datetime.now().second

year = perthyearnow - \
    datetime.datetime(perthyear, perthmonth, perthday).date().year
month = perthmonthnow - \
    datetime.datetime(perthyear, perthmonth, perthday).date().month
day = perthdaynw - \
    datetime.datetime(perthyear, perthmonth, perthday).date().day
hour = perthhournow - \
    datetime.datetime(perthyear, perthmonth, perthday, perthhour).time().hour
second = perthsecondnow - \
    datetime.datetime(perthyear, perthmonth, perthday,
                      perthhour, perthsecond).time().second


print(
    f"your age is {year} year and {month} month and {day} day and {hour} hour and {second}  second")
