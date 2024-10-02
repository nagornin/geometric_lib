import math


def area(r):
    '''
    Returns area of a circle with radius r

    Example usage:
    > area(2)
    12.566370614359172
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Returns perimiter of a circle with radius r

    Example usage:
    > perimiter(3)
    18.84955592153876
    '''
    return 2 * math.pi * r

