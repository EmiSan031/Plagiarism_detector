def circle_area(radius):
    pi = 3.14159265
    return pi * radius * radius

def circle_perimeter(radius):
    pi = 3.14159265
    return 2 * pi * radius

def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return 2 * (width + height)

def shapes_report(radius, width, height):
    c_area = circle_area(radius)
    c_perim = circle_perimeter(radius)
    r_area = rectangle_area(width, height)
    r_perim = rectangle_perimeter(width, height)
    print(f"--- Circle (r={radius}) ---")
    print(f"  Area            : {c_area:.4f}")
    print(f"  Perimeter       : {c_perim:.4f}")
    print(f"--- Rectangle ({width}x{height}) ---")
    print(f"  Area            : {r_area}")
    print(f"  Perimeter       : {r_perim}")
    print(f"Larger area     : {'circle' if c_area > r_area else 'rectangle'}")
    return c_area, r_area

shapes_report(5, 4, 6)
