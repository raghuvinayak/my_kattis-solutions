check = ["none",'A','B','C']

a = input()
b = list(a)


if b[0] == "C":
    output = 3
elif b[0] == "B":
    output = 2
else:
    output = 1

for i in range(0,len(b)):
    if i == (len(b) -1):
        break
    if check.index(b[i]) < check.index(b[i+1]):
        output += check.index(b[i+1])
    elif check.index(b[i]) == check.index(b[i+1]):
        continue
    else:
        output -= check.index(b[i+1])

print(output)
