my_list = []
while True:

    start_with_limit = int(input())

    t2 = 0
    sum = 0
    if start_with_limit == -1:
        print(*my_list, sep="\n")
        break
    else:
        for i in range(0, start_with_limit):
            time_one = input()
            my_input = time_one.split(" ")
            speed = int(my_input[0])
            t1 = int(my_input[1])
            time = t1 - t2
            i += 1
            time_travell = (speed * time)
            sum += time_travell
            t2 = t1
            my_value = str(sum) + " miles"
        my_list.append(my_value)
