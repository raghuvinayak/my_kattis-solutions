a,b = [int for int in input().split()]
list_1 = []
for i in range(int(a)):
    for j in range(int(b)):
        data = input()
        list(data)
        # print(data)
        if data[0].lower() + data[1:] == data.lower():
            list_1.append(1)
print(max(list_1), sep='')
