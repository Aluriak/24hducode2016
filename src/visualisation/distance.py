"""
Computes distances between two points from their Gmap coordinates
"""

from math import radians, cos, sin, asin, sqrt


def distance_gps(coordinates_A, coordinates_B):
    """
    Input: two tuples of coordinates (longitude, latitude)
    Output: distance between the two points
    """
    lon1 = coordinates_A[0]
    lat1 = coordinates_A[1]
    lon2 = coordinates_B[0]
    lat2 = coordinates_B[1]

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# Usage example
# test = distance_gps((-0.0693341, 47.6971825), (0.24142796, 47.9908779))
# print(test)
