monthly_limit = int(input())
number_of_months = int(input())

remaining_data = 0

for i in range (0, number_of_months):
    data_used_monthly = int(input())
    next_month = (remaining_data + monthly_limit)
    remaining_data = (next_month - data_used_monthly)
    i += 1

print(remaining_data + monthly_limit)
