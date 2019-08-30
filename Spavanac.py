data = input()
time_ = data.split(" ")
hour = int(time_[0])
minutes = int(time_[1])

if minutes < 45:
    minutes += 15
    if hour < 1:
        hour = 23
    else:
        hour = hour - 1
else:
    minutes -= 45

print(str(hour)+" "+str(minutes))
