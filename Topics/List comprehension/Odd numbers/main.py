string_list = list(input())
integer_list = [int(x) for x in string_list]
odd_nums = [x for x in integer_list if x % 2 != 0]
print(odd_nums)
