num_list = list(input())
digits_list = [int(x) for x in num_list]
mean = sum(digits_list) / len(digits_list)
print(mean)