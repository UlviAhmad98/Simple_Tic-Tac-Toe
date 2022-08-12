# please work with the variable 'list_of_strings'
# list_of_strings = ["36", "45", "99"]
integer_strings = [int(x) for x in list_of_strings]
number_list = [int(x) + 1 for x in list_of_strings]
print(number_list)