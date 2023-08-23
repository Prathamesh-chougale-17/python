# dictionaries

dict = {
    "name": [1, 2, 3],
    "content": {3, 6, 4, 5, 3, 8},
    "help": (9, 1, 1),
    "nothing": "feeling good",
}

print(dict)

# lookup

print(dict["name"])

dict["graduation"] = 1985

print(dict)

# del value

del dict["name"]
print(dict)

# check value
check_value = "content" in dict
print(check_value)
