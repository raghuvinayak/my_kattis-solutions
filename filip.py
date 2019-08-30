enter_input = input()
a = enter_input.split(" ")
part1 = a[0]
part2 = a[1]
a = part1[::-1]
b = part2[::-1]
if a > b:
    print(a)
else:
    print(b)
