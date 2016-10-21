import math
from math import radians, cos, sin, asin, sqrt

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx*dx + dy*dy)

def local_distance(point1, point2):
    """ Just to show how package namespaces work"""
    pass

def nearest_airport(origin_id, points):
    # don't calculate d_{i,i}
    distance = math.inf
    nn_id = math.inf
    i = origin_id
    for j, point in enumerate(points):
        d_ip = euclidean_distance(points[i], point)
        if d_ip != 0:
            if d_ip < distance:
                distance = d_ip
                nn_id = j
    return origin_id,nn_id, distance

def nearest_airport_h(origin_id, points):
    # don't calculate d_{i,i}
    distance = math.inf
    nn_id = math.inf
    i = origin_id
    for j, point in enumerate(points):
        d_ip = haversine(points[i], point)
        if d_ip != 0:
            if d_ip < distance:
                distance = d_ip
                nn_id = j
    return origin_id,nn_id, distance

def haversine(point1,point2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1,lat1 = point1
    lon2,lat2 = point2
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r