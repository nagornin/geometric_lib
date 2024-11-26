import math
import numbers


def area(r):
    '''
    Returns area of a circle with radius r

    Example usage:
    > area(2)
    12.566370614359172
    '''

    if not isinstance(r, numbers.Real):
        raise TypeError("Circle radius must be a real number")

    if not math.isfinite(r):
        raise ValueError("Circle radius must be a finite number")

    if r < 0:
        raise ValueError("Circle radius must be non-negative")

    return math.pi * r * r


def perimeter(r):
    '''
    Returns perimiter of a circle with radius r

    Example usage:
    > perimiter(3)
    18.84955592153876
    '''

    if not isinstance(r, numbers.Real):
        raise TypeError("Circle radius must be a real number")

    if not math.isfinite(r):
        raise ValueError("Circle radius must be a finite number")

    if r < 0:
        raise ValueError("Circle radius must be non-negative")

    return 2 * math.pi * r

