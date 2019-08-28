my_input = int(input())
my_list2 = []
my_list3 =[]
my_list4 = []
for i in range(0, my_input):
    my_val222 = input()
    my_list2 = my_val222.split(" ")
    i+=1
    for j in range(0, 100):
        in_ques = input()
        var1 = in_ques.split(" ")
        j+=1
        if var1[-1] == "say?":
            break
        else:
            var2 = var1[-1]
            my_list3.append(var2)
    my_var = ''
    for i in range(0, len(my_list2)):
        if my_list2[i] in my_list3:
            continue

        else:
            my_var += my_list2[i] + ' '
            i+=1
    my_list4.append(my_var)
print(*my_list4, sep=" \n")
