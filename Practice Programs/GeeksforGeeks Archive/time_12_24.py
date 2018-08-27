# Python program to convert time from 12 hour to 24 hour format

def time_12_24(time_12):
  hh = int(time_12[0:2])
  meridian = time_12[6:11]
  if meridian == "PM":
    time_24 = str(hh+12) + time_12[2:5]
  else:
    if hh == 12:
      hh = 0
    time_24 = str(hh) + time_12[2:5]
  return time_24

time_12 = input("Enter time(hh:mm AM/PM): ")
print(time_12_24(time_12))
