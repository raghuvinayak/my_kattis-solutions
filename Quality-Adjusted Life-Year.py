number_of_periods = int(input())
sum = 0
for i in range(0, number_of_periods):
    my_first = input()
    my_input = my_first.split(" ")
    quality_of_life = float(my_input[0])
    number_of_years = float(my_input[1])
    my_first_value = quality_of_life * number_of_years
    i += 1

    sum += my_first_value


print(round(sum,3))
