for i in range(int(input())):
    x, y = [int(x) for x in input().split()]
    a,b,c = int((y*(y+1))/2),y**2,y*(y+1)
    print("{} {} {} {}".format(x,a,b,c))
