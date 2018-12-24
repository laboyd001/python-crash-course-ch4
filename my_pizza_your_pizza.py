#add a new pizza to the list, add a different pizz to friends list, prove you have two lists

pizzas = ['cheese', 'peperoni', 'supreme']
friends_pizzas = pizzas[:]
pizzas.append('mushroom')
friends_pizzas.append('bbq')

print("My favorite pizzas are:")
for pizza in pizzas:
 print(pizza)
print("\nMy friends favorite pizzas are:")
for pizza in friends_pizzas:
 print(pizza)
