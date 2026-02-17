from point import Point
from orientation import orientation

def monotone_chain(points: list[Point]):
    if points == 0:
        return []

    # O(nlogn)
    # Sort by x with y tiebreaker
    points_sorted_x = sorted(points, key=lambda x: (x.x, x.y))

    # Find lower hull
    lower = []
    for p in points_sorted_x:
        while (len(lower) >= 2 and orientation(lower[-2], lower[-1], p) >= 0):
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points_sorted_x):
        while (len(upper) >= 2 and orientation(upper[-2], upper[-1], p) >= 0):
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
