x = range(4)
print(list(x))

for i in range(4):
    print(i)

square = ["red", "yellow", "green", "purple", "blue"]

for i in range(0, 5):
    print("Before square", i, "is", square[i])
    square[i] = "white"
    print("After square", i, "is", square[i])

# without index

square = ["red", "yellow", "green", "purple", "blue"]
for square in square:
    print(square)

# enumerate

for i, square in enumerate(square):
    print(i, square)

# while loop

square = ["yellow", "yellow", "green", "yellow", "blue"]
new_square = []
i = 0
while square[i] == "yellow":
    new_square.append(square[i])
    i = i + 1

print(new_square)
