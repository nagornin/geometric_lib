import math
import numbers

def area(a, b):
    '''
    Returns area of a rectangle with sides a and b

    Example usage:
    > area(4, 3)
    12
    '''

    if not all(isinstance(x, numbers.Real) for x in [a, b]):
        raise TypeError("Rectangle sides must be real numbers")

    if not all(math.isfinite(x) for x in [a, b]):
        raise ValueError("Rectangle sides must be finite numbers")

    if a < 0 or b < 0:
        raise ValueError("Rectangle sides must be non-negative")

    return a * b

def perimeter(a, b):
    '''
    Returns perimiter of a rectangle with sides a and b

    Example usage:
    > perimiter(7, 4)
    22
    '''

    if not all(isinstance(x, numbers.Real) for x in [a, b]):
        raise TypeError("Rectangle sides must be real numbers")

    if not all(math.isfinite(x) for x in [a, b]):
        raise ValueError("Rectangle sides must be finite numbers")

    if a < 0 or b < 0:
        raise ValueError("Rectangle sides must be non-negative")

    return (a + b) * 2
