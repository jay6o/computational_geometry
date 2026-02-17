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

    # Create a hard copy with new point objects so we don't change the original
    polar_plane = []
    for p in points:
        polar_plane.append(p.copy())

    # O(n)
    # Transform plane so that base point is (0,0)
    for p in polar_plane:
        p.x -= base_p.x
        p.y -= base_p.y 

    # O(n)
    # Calculate angles from base_p_polar
    polar_angles_from_base = []
    for p in polar_plane:
        theta = math.atan2(p.y, p.x)
        polar_angles_from_base.append(theta)

    # O(nlgn)
    # Use a mapping+lambda function to sort the original array by the polar angle
    original_polar = zip(points, polar_angles_from_base)
    sorted_counter_clockwise = [k for k,val in sorted(original_polar, key=lambda x: x[1])]

    gs_stack = [base_p]
    # O(n) due to amortization (n items can only be pushed/popped once)
    for p in sorted_counter_clockwise:
        if len(gs_stack) < 2:
            gs_stack.append(p)
        else:
            # check orientation, if clockwise pop off the stack until CC
            p1, p2, = gs_stack[-2], gs_stack[-1]
            o = orientation(p1, p2, p)
            if o <= 0: # CC or Colinear
                gs_stack.append(p)
            else:
                clockwise = True
                # O(n)
                while(clockwise):
                    gs_stack.pop()
                    if len(gs_stack) < 2: # We can pop to less than 2 p
                        gs_stack.append(p)
                        break
                    p1, p2, = gs_stack[-2], gs_stack[-1]
                    o = orientation(p1, p2, p)
                    if o <= 0: # CC or Colinear
                        gs_stack.append(p)
                        clockwise = False
    return gs_stack
