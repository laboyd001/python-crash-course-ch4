#this program demos iterating through a range of exponents

# squares = []
# for value in range(1,11):
#   square = value**2
#   squares.append(square)

# print(squares)

#more concise code:
# squares = []
# for value in range(1,11):
#   squares.append(value**2)

# print(squares)

#functions specific to numbers:

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

#list comprehension example:

squares = [value**2 for value in range(1,11)]
print(squares)