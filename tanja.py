data = input().split()
if len(data)<=3:
    print(data)
elif 4 <= len(data) <= 15:
    c = (list(data))
    odd = c[::2]
    even = c[1::2]
    daa = odd+even
    out = ""
    for x in daa:
        out+=x
    print(out)
else:
    my_list = list(data)
    row1 = my_list[::4]
    row2 = my_list[1::4]
    row3 = my_list[2::4]
    row4 = my_list[3::4]
    output = row1+row2+row3+row4
    out1 = ""
    for y in output:
        out1+=y
    print(out1)
