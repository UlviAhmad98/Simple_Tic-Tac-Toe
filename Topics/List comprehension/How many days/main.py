seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
days = [sec // 86400 for sec in seconds]
print(days)
