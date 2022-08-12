# work with a list from this variable
numbers = [int(n) for n in input()]

# change the next two lines
less_than_5 = [value for value in numbers if value < 5]
greater_than_5 = [value for value in numbers if value > 5]

# printing your results
print(less_than_5)
print(greater_than_5)
