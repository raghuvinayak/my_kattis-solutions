import math
my_data = input()
my_list = my_data.split(" ")
height = int(my_list[0])
angle = int(my_list[1])
ladder = math.ceil(height/math.sin(math.radians(angle)))
print(ladder)
