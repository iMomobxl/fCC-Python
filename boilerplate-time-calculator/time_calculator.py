def add_time(start, duration, day=""):
  # Splitting the start time into hours, minutes and AM/PM
  start_time = start.split()
  duration_time = duration.split(":")
  time = start_time[0].split(":")
  
  # add duration to time
  for i in range(len(time)) :
    time[i] = str(int(time[i]) + int(duration_time[i]))
  
  count_days = 0
  count_hours = 0
  
  # time[0] = hours & time[1] = minutes
  while int(time[1]) > 60:
    time[1] = str(int(time[1]) - 60)
    time[0] = str(int(time[0]) + 1)
  while int(time[0]) >= 12:
    time[0] = str(int(time[0]) - 12)
    count_hours +=1
  if int(time[0]) == 0:
      time[0] = "12"

  # setting the correct AM PM
  while count_hours > 0:
    if start_time[1] == "AM":
      start_time[1] = "PM"
    else:
      start_time[1] = "AM"
      count_days += 1
    count_hours -= 1
    
  # add "0" to minutes  
  if len(time[1]) != 2:
    time[1] = "0" + time[1]

  # set new_time
  new_time = time[0] + ":" + time[1] + " " + start_time[1]
  
  # check day if is set
  if day != "":
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    index = days_list.index(day.lower().title()) + count_days
    while index > 6:
      index -= 7
    new_time = new_time + ", " + days_list[index]

  # add the number of days
  if count_days == 1:
    new_time = new_time + " (next day)"
  elif count_days > 1:
    new_time = new_time + " (" + str(count_days) + " days later)"
  
  return new_time