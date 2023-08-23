# set are a type of collection
set1 = {2, 5, 3, 6, 8, 7, 5, 3, 2, 1}
print(set1)  # set automatically sort and remove duplicate element

# typecasting

list1 = [1, 2, 4, 3, 2, 5, 5]
print(list1)

set1 = set(list1)
print(set1)

# set operation{vein diagram}

set_a = {1, 4, 3, 2, 1, 6}
print(set_a)

set_a.add(2)
print(set_a)

set_a.remove(3)
print(set_a)

check_value = 2 in set_a
print(check_value)

check_value = 9 in set_a
print(check_value)

set_x = {1, 2, 7, 6, 3, 7, 9}
print(set_x)

set_y = {2, 5, 1, 7, 3, 8}
print(set_y)

# and operation
set_z = set_x & set_y
print(set_z)

# or operation

set_w = set_x | set_y
print(set_w)

check_subset = set_x.issubset(set_w)
print(check_subset)
