# creating own classes without __init__ function


class rectangle(object):
    length = 9
    color = "red"


class circle(object):
    radius = 19
    color = "blue"


circle = circle()
rectangle = rectangle()

print(circle.radius)
print(rectangle.length)
print(circle.color)
print(rectangle.color)

# with __init__ function it is an constuctor


class triangle(object):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.color = "green"

    # def drawtriangle(self):


triangle = triangle(10, 20)
print(triangle.base)
print(triangle.height)
print(triangle.color)


# methods
class rectangle1(object):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def area(self):
        # print(self.breath * self.length)
        return self.breath * self.length


rectangle1 = rectangle1(5, 6)

print(rectangle1.length)
print(rectangle1.breath)
# rectangle1.area()
print(rectangle1.area())
