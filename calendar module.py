# to creat the years of calendarS

import calendar
yy=2022  # year
mm= 12   # month
 
# to take month and year input from the user



yy = int(input("Enter year:"))
mm = int(input("Enter month:"))
print(calendar.month(yy,mm))
