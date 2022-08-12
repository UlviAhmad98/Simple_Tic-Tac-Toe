def average(number_1, number_2):
    return (number_1 + number_2) / 2


average_list = [average(x, x + 1) for x in range(1, len(list(input())))]
print(average_list)
