def taxicab_distance_nd(point1, point2):
    """
    Calculates Taxicab (Manhattan) distance between two points in n dimensional space

    Parameters:
        point1: tuple
            Coordinates of the first point (x1, x2, x3,...,xn)
        point2: tuple 
            Coordinates of the second point (y1, y2, y3,...,yn)

    Returns:
        distance: int/float
            Taxicab distance between the two points
    """
    
    distance = 0
    for x, y in zip(point1, point2):
        distance += abs(y - x)
    
    # Single line taxicab distance calculation
    # distance = sum(abs(y - x) for x, y in zip(point1, point2))

    return distance


point_a = (2, 3, 5)
point_b = (7, 5, 9)
distance = taxicab_distance_nd(point_a, point_b)
print(f"Taxicab/Manhattan distance between {point_a} and {point_b} in 3D is {distance}")
