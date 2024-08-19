import math

def euclidean_distance(point1, point2):
    """
    Calculates Euclidean distance between two points in 2 dimensional space

    Parameters:
        point1: tuple
            Coordinates of the first point (x1, y1)
        point2: tuple
            Coordinates of the second point (x2, y2)

    Returns:
        float
            euclidean distance between the two points
    """

    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distance

point_a = (2, 3)
point_b = (7, 5)
distance = euclidean_distance(point_a, point_b)
print(f"Euclidean distance between {point_a} and {point_b} is {distance}")