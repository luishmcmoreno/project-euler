starting_day = 2
day = 1
month = 1
year = 1901

sundays = 0
while (year < 2001):
  if (day == 1 and starting_day % 7 == 0):
    sundays += 1
  day += 1
  starting_day += 1
  if (month == 2):
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
      if (day == 30):
        day = 1
        month = 3
    else:
      if (day == 29):
        day = 1
        month = 3
  elif (month == 4 or month == 6 or month == 9 or month == 11):
    if (day == 31):
      day = 1
      month += 1
  else:
    if (day == 32):
      day = 1
      month += 1
  if (month == 13):
    month = 1
    day = 1
    year += 1
print sundays