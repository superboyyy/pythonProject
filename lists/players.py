players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[-3:])

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

print("\nThe first three items in the list are:")
for i in players[:3]:
    print(i.title())

print("\nThree items from the middle of the list are:")
for i in players[1:4]:
    print(i.title())

print("\nThe last three items in the list are:")
for i in players[-1:-4:-1]:
    print(i.title())