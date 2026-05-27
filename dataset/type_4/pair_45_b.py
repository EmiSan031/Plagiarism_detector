import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius

def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return 2 * (width + height)

def triangle_area(base, height):
    return 0.5 * base * height

def hypotenuse(a, b):
    return math.hypot(a, b)

def degrees_to_radians(degrees):
    return math.radians(degrees)

print(circle_area(5))
print(circle_perimeter(5))
print(rectangle_area(4, 6))
print(triangle_area(3, 8))
print(hypotenuse(3, 4))
print(degrees_to_radians(180))
