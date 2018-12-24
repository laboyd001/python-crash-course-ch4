#make a list of the first 10 cubes and use a for loop to print them

cubes = []
for value in range(1,11):
  cube = value**3
  cubes.append(cube)
print(cubes)