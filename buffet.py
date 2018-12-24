# use a for loop to print each food, try to modify one item, add code to rewrite the tuple

buffet = ('salad', 'ham', 'chicken', 'pizza', 'rolls')
for food in buffet:
    print(food)


# Cannot modify one item:
# buffet[0] = ('jello')
# for food in buffet:
#   print(food)

print("\nUpdate buffet menu:")
buffet = ('salad', 'ham', 'egg salad', 'soup', 'rolls')
for food in buffet:
    print(food)
