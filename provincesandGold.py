data1 = input()
data = data1.split(" ")
gold = int(data[0])
silver = int(data[1])
copper = int(data[2])
my_list = []
sum_of = (gold * 3) + (silver * 2) + (copper)

if sum_of > 7:
    my_list.append("Province")
elif sum_of > 4:
    my_list.append("Duchy")
elif sum_of > 1:
    my_list.append("Estate")

if sum_of > 5:
    my_list.append("Gold")
elif sum_of > 2:
    my_list.append("Silver")
else:
    my_list.append("Copper")

print(" or ".join(my_list))
