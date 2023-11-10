class Circle():
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2*3.14*self.radius
    
    def area(self):
        return 3.14*self.radius**2
    
radius = 5
circle = Circle(radius)

area = circle.area()

perim = circle.perimeter()

print(area)

class Person():
    def __init__(self, name, country, birth):
        self.name = name
        self. country = country
        self.birth = birth

    def age(self):
        return 2023-self.birth

person1 = Person("peter", "bagdad", 25)

print(person1.age())

class Shape():
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radisu = radius

    def calculate_area(self):
        return 3.14*self.radius**2
    
    def calculate_perimeter(self):
        return 2*3.14*self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    
rectangle = Rectangle()

print(rectangle.area(7, 76))