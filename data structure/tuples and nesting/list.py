# list are a;sp ordered sequence
# list is represented in square bracket []
list = [2, 3, 454, "prathamesh", 7.45, ("a", "b", "c")]
# print(len(list))
# print(list[5][2])
# print(list[3:5])
# print(list[2:6])
# print(list[1:4:2])
list_1 = ["prakash", 34.2]
list_3 = list + list_1
print(list_3)
list_2 = ["pratik", 75]
list_3.append(list_2)
print(list_3)
# list are mutable{can be changed}
del list_3[3]
print(list_3)  # info: del is used to delete the element from the list
list_5 = "prathamesh Chougale".split()
print(list_5)

# aliasing

a = ["prathamesh", 10, 1.2]
b = a
print(a)
b[0] = "pratik"
print(a)

# cloning

c = a[:]
print(c)

help(a)
# print(a)
