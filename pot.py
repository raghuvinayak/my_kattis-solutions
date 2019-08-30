x = int(input())
n = 0
for i in range(0, x):
    power = input()
    a = int(power[-1])
    b = int(power[:-1])
    sum_ = (b ** a)
    n += sum_
    i+=1
print(n)
