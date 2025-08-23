import datetime


#creating datetime object with current date and time
x = datetime.datetime.now()
print(x)
print(type(x))
print()

#adding 1 day to today's datetime object
x = datetime.datetime.now() + datetime.timedelta(days=1)
print(x)
print(type(x))
print()

#creating datetime object with given year, month & day
x = datetime.datetime(2020, 5, 17)
print(x)
print(type(x))
print()

#return the name of the day (string) of the datetime object's date, e.g. Monday, Tuesday etc.
x = datetime.datetime.now().strftime("%A")
print(x)
print(type(x))
print()

#return the date of the datetime object in YYYY-MM-DD (string)
x = datetime.datetime.now().strftime("%Y-%m-%d") 
print(x)
print(type(x))
print()
