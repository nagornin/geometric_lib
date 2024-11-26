import math
import numbers

def area(a, h):
    '''
    Returns area of a triangle with base a and height h

    Example usage:
    > area(4, 5)
    10
    '''

    if not all(isinstance(x, numbers.Real) for x in [a, h]):
        raise TypeError("Triangle sides must be real numbers")

    if not all(math.isfinite(x) for x in [a, h]):
        raise ValueError("Triangle sides must be finite numbers")

    if a < 0 or h < 0:
        raise ValueError("Triangle sides must be non-negative")

    return a * h / 2

def perimeter(a, b, c):
    '''
    Returns perimiter of a triangle given sides a, b, c

    Example usage:
    > perimiter(1, 2, 3)
    6
    '''

    if not all(isinstance(x, numbers.Real) for x in [a, b, c]):
        raise TypeError("Triangle sides must be real numbers")

    if not all(math.isfinite(x) for x in [a, b, c]):
        raise ValueError("Triangle sides must be finite numbers")

    if a < 0 or b < 0 or c < 0:
        raise ValueError("Triangle sides must be non-negative")

    return a + b + c
