PI = 3.141592653589793

def circle_area(radius):
    return PI * radius * radius

def circle_perimeter(radius):
    return 2 * PI * radius

def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return 2 * (width + height)

def triangle_area(base, height):
    return 0.5 * base * height

def hypotenuse(a, b):
    return (a * a + b * b) ** 0.5

def degrees_to_radians(degrees):
    return degrees * PI / 180

print(circle_area(5))
print(circle_perimeter(5))
print(rectangle_area(4, 6))
print(triangle_area(3, 8))
print(hypotenuse(3, 4))
print(degrees_to_radians(180))
