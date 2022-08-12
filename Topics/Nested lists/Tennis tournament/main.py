games = int(input())
new_list = []
for n in range(games):
    new_list.append(input())
winner_list = []
for winner in new_list:
    if winner.endswith("win"):

        winner_list.append(winner.split()[0])

print(winner_list)
print(len(winner_list))
        