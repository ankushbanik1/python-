import calendar
x=calendar.calendar(2018)
print(x)
y=calendar.month(2019,3)
print(y)

if(calendar.isleap(2022)):
    print("leapyear")
else:
    print("not leapyear")   