def disk_area(r):
    if r < 0:
        return None
    pi = 3.14159265
    return pi * r * r

def disk_circumference(r):
    if r < 0:
        return None
    pi = 3.14159265
    return 2 * pi * r

def quad_area(w, h):
    if w < 0 or h < 0:
        return None
    return w * h

def quad_perimeter(w, h):
    if w < 0 or h < 0:
        return None
    return 2 * (w + h)

def triangle_area(base, height):
    if base < 0 or height < 0:
        return None
    return 0.5 * base * height

def geometry_report(r, w, h):
    d_area = disk_area(r)
    d_circ = disk_circumference(r)
    q_area = quad_area(w, h)
    q_perim = quad_perimeter(w, h)
    t_area = triangle_area(w, h)
    print(f"--- Disk (r={r}) ---")
    print(f"  Area            : {d_area:.4f}")
    print(f"  Circumference   : {d_circ:.4f}")
    print(f"--- Quadrilateral ({w}x{h}) ---")
    print(f"  Area            : {q_area}")
    print(f"  Perimeter       : {q_perim}")
    print(f"--- Triangle (b={w}, h={h}) ---")
    print(f"  Area            : {t_area}")
    print(f"Larger area     : {'disk' if d_area > q_area else 'quad'}")
    return d_area, q_area

geometry_report(5, 4, 6)
