my_num = 0
data = int(input())
for i in range(int(input())):
    w, l = input().split()
    my_num += (int(w)*int(l))
print(int(my_num/data))
