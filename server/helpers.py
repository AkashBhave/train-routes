from math import pi, acos, sin, cos


def calc_distance(y1, x1, y2, x2):
    """
    Calculate distance between two locations using great circle distance.

    Notes:
        y1 = lat1, x1 = long1
        y2 = lat2, x2 = long2
        all assumed to be in decimal degrees

        if (and only if) the input is strings
        use the following conversions
    """

    if y1 == x1 == y2 == x2:
        return float(0)

    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)

    R = 3958.76  # miles = 6371 km

    y1 *= pi / 180.0
    x1 *= pi / 180.0
    y2 *= pi / 180.0
    x2 *= pi / 180.0

    # approximate great circle distance with law of cosines
    return acos(sin(y1) * sin(y2) + cos(y1) * cos(y2) * cos(x2 - x1)) * R
