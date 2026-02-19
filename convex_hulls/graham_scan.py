import math
from point import Point
from orientation import orientation

def graham_scan(points: list[Point]):
    if len(points) == 0:
        return []

    # O(n)
    # Pick lowest y or tiebreak with lowest x
    base_p = Point(0, float("inf"))
    for p in points:
        if base_p.y > p.y:
            base_p = p
        elif base_p.y == p.y: # Tiebreaker
            if base_p.x > p.x:
                base_p = p

    # O(n)
    # Remove base for sorting and copy
    points.remove(base_p)


    # O(nlgn)
    # Sort by the polar angle around base
    sorted_counter_clockwise = sorted(points, key=lambda p: math.atan2(p.y - base_p.y, p.x - base_p.x))

    gs_stack = [base_p]
    # O(n) due to amortization (n items can only be pushed/popped once)
    # Loop through sorted list and build convex hull
    for p in sorted_counter_clockwise:
        while len(gs_stack) >= 2 and (orientation(gs_stack[-2], gs_stack[-1], p) > 0):
            gs_stack.pop()
        gs_stack.append(p)
    return gs_stack
