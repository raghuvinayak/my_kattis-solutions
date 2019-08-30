my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
for i in range(0,3):
    my_input = input()
    a = my_input.split(" ")
    rectangle_one = int(a[0])
    rectangle_two = int(a[1])
    i += 1
    my_list1.append(rectangle_one)
    my_list2.append(rectangle_two)
    
if my_list1[0] != my_list1[1] and my_list1[0] != my_list1[2]:
    my_list3.append(my_list1[0])

if my_list1[1] != my_list1[0] and my_list1[1] != my_list1[2]:
    my_list3.append(my_list1[1])

if my_list1[2] != my_list1[0] and my_list1[2] != my_list1[2]:
    my_list3.append(my_list1[2])
    
if my_list2[0] != my_list2[1] and my_list2[0] != my_list2[2]:
    my_list4.append(my_list1[0])

if my_list2[1] != my_list2[0] and my_list2[1] != my_list2[2]:
    my_list4.append(my_list2[1])

if my_list2[2] != my_list2[0] and my_list2[2] != my_list2[1]:
    my_list4.append(my_list2[2])

print(my_list3[0], my_list4[0])
