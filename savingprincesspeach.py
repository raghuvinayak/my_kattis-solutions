a,b = [int for int in input().split()]
my_set = set()
my_range = set([x for x in range(int(a))])
for i in range(int(b)):
    data = int(input())
    my_set.update([data])
difference =  my_range - my_set
for j in difference:
    print(j)
print("Mario got {} of the dangerous obstacles.".format(len(my_set)))
