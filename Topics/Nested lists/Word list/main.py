text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
new_list = []
user = int(input())
for word in text:
    for index in word:
        if len(index) <= user:
            new_list.append(index)
print(new_list)
