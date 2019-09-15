for x in range(int(input())):
    a = (x + 1)
    data = int(input())
    data2 = [int(x) for x in input().split()]
    given_22 = set(data2)
    given_d = list(data2)
    for x in given_d:
        if given_d.count(x) <= 1:
            output = int(x)
    print("Case #{}: {}".format(a, output))
