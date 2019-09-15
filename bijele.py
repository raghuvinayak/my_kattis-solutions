old_chess = [1, 1, 2, 2, 2, 8]
my_data = input()
a = list(my_data.split( ))
my_int = [int(i) for i in a]
list_demo = []
for i in range(0,len(a)):
    list_demo.append (old_chess[i] - my_int[i])
    i+=1
print(*list_demo)
