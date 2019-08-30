x = int(input())
y = input()
z = y.split(" ")
b = []
sum = 0
for i in range(0, len(z)):
    if z[i] == "-1":
        continue
    else:
        b.append(z[i])
    i+=1
for j in range(0,len(b)):
    sum+= int(b[j])
    j+=1

print(sum/len(b))
