data = input()
datas = data.split(" ")
N = int(datas[0])
M = int(datas[1])
a = min(N,M)
b = max(N,M)
for i in range(a+1, b+2):
    if N == M:
        print(N + 1)
    elif N != M:
     print(i)
    i+= 1
