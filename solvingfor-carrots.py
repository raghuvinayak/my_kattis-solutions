x = input()
a = x.split(" ")
required_inputs = int(a[0])
carrots_required = int(a[1])

if required_inputs >= 1 and carrots_required <= 1000:
    for i in range(0, required_inputs):
        my_input = (input())
        i+=1
    print(int(carrots_required))
