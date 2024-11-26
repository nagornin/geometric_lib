import math
import numbers

def area(a):
    '''
    Returns area of a square with side length a

    Example usage:
    > area(3)
    9
    '''

    if not isinstance(a, numbers.Real):
        raise TypeError("Square side must be a real number")

    if not math.isfinite(a):
        raise ValueError("Square side must be a finite number")

    if a < 0:
        raise ValueError("Square side must be non-negative")

    return a * a


def perimeter(a):
    '''
    Returns perimiter of a square with side length a

    Example usage:
    > perimiter(2)
    8
    '''

    if not isinstance(a, numbers.Real):
        raise TypeError("Square side must be a real number")

    if not math.isfinite(a):
        raise ValueError("Square side must be a finite number")

    if a < 0:
        raise ValueError("Square side must be non-negative")

    return 4 * a
