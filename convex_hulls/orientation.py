from point import Point

def orientation(p1: Point, p2: Point, p3: Point):
    x1, y1 = (p1.x, p1.y)
    x2, y2 = (p2.x, p2.y)
    x3, y3 = (p3.x, p3.y)

    return ((y2 - y1) * (x3 - x2)) - ((y3 - y2) * (x2 - x1))


