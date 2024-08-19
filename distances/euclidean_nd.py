import math

def euclidean_distance_nd(point1, point2):
    """
    Calculates Euclidean distance between two points in n dimensional space

    Parameters:
        point1: tuple/list
            Coordinates of the first point
        point2: tuple/list 
            Coordinates of the second point

    Returns:
        distance: float
            Euclidean distance between the two points
    """
    distance = 0

    for x1, x2 in zip(point1, point2):
        distance += (x2 - x1)**2
    
    distance = math.sqrt(distance)

    # Single line manhattan distance calculation
    # distance = math.sqrt(sum((x2 - x1)**2 for x1, x2 in zip(point1, point2)))

    return distance

point_a = (2, 3, 5)
point_b = (7, 5, 9)
distance = euclidean_distance_nd(point_a, point_b)
print(f"Euclidean distance between {point_a} and {point_b} in 3D is {distance}")
