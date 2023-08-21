tuple1 = ("prathamesh",43,"pratik")
# print(tuple[2])
# print(tuple[1])
# print(tuple[0])
tuple2 = ("pratik",75) + tuple1   # it work
print(tuple2)
# print(("pratik",75) + tuple1)   # it works
# print(tuple2[0])      #it works # it print element at position at 0 in tuple2 
# print(tuple2[1])      #it works
# print(tuple2[2])      #it works
# print(tuple2[3])      #it works
# print(tuple2[4])      #it works
# print(tuple2[5])      #it works
# print(tuple2[0:2])    #it works
# print(tuple2[2:5])    #it works
print(tuple2[::2])    #it works
# print(tuple2[:4:2])   #it works
print(tuple2[1:4:2])  #it works
# tuple3 = sorted(tuple1) #not works as there is string present
# tuple4 = sorted(tuple2)   #not works as there is string present
# tuple5 = (5,5,7,4,9,4,2,2,5,1,7)
# tuple6 = (67,3,54,23,67,74,83)
# tuple7 = sorted(5,5,7,4,9,4,2,2,5,1,7) # not works as there should not be more than 1 element in sorted() 
# tuple8 = sorted(tuple6) #it works as there is only one element in sorted() 
# print(tuple7)
# print(tuple8)