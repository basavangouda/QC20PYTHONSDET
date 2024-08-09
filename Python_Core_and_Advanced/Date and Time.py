import datetime

# Case 1 get the Current Date and Time
now=datetime.datetime.now()
print(now)

# Case 2 get the Current Date and Time
#from datetime import datetime
#now=datetime.now()
#print(now)

#Get current Date
cur_date=datetime.date.today()
print(cur_date)

# Get the date time stamp
timestamp=datetime.date.fromtimestamp(1722904615)
print("Date :",timestamp)

#Get the Month, date and Year
today=datetime.date.today()
print("Current Year :",today.year)
print("Current Month :",today.month)
print("Current day :",today.day)

#I want to pass Hour,Minute, Second and Micro Second and print it
a=datetime.time(11,34,56)
print("Hour :",a.hour)
print("Minute :",a.minute)
print("Second :",a.second)
print("Microsecond :",a.microsecond)

#Handling timezone in Python
import pytz

local=datetime.datetime.now()
print("Local :",local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY=pytz.timezone('America/New_York')
datetime_NY=datetime.datetime.now(tz_NY)
print(datetime_NY)
print("NY Time :",datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))