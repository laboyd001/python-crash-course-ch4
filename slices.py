#add several lines to the end of a program one that prints the first 3 items, one that prints items from the middle, and one that prints items from the end

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nThe first 3 items in the list are:")
for player in players[:3]:
  print(player.title())

print("\nThe middle players are:")
for player in players[1:4]:
  print(player.title())

print("\nThe end players are:")
for player in players[-3:]:
  print(player.title())