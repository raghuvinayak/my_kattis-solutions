a =input()
b = input()
cipher = list(a)
key = list(b)
my_aplha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cracker = list(my_aplha)
output = ""

for i in range(0,len(cipher)):
    my_valuation = (cracker.index(cipher[i])) - (cracker.index(key[i]))
    key.append(cracker[my_valuation])
    i+=1
    output += cracker[my_valuation]

print(output)
