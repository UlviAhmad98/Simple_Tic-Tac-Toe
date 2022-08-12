value_list = [int(x) for x in list(input())]
running_total = [sum(value_list[:value + 1]) for value in range(len(value_list))]
print(running_total)
