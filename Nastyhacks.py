data = int(input())
for i in range(0, data):
    my_advert = input()
    a = my_advert.split(" ")
    my_integer = int(a[0])
    if my_integer == 0:
        print("advertise")
    elif my_integer < 0:
        print("do not advertise")
    elif my_integer > 0:
        print("does not matter")
    i+=1
