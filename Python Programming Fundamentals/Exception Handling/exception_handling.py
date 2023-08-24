try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("division by zero")
except:
    print("other exception")
finally:
    print("finally")
print("nice day")
