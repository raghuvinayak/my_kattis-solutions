my_list = []
my_list1 = []
for i in range(0,5):
    datas = input()
    data = datas.split(" ")
    data = list(map(int, data))
    a = sum(data)
    my_list1.append(a)
    my_list.append(data)
    i+=1
max_index = my_list1.index(max(my_list1))
print(max_index +1,max(my_list1))
