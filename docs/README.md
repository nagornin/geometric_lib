# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Documentation

This library provides functions for calculating area and perimiter of various geometric shapes. The implementation for each shape is located in a separate file.

## Triangle

### Area

`area(a, h)`

Returns area of a triangle with base `a` and height `h`

```
> area(4, 5)
10
```

### Perimiter

`perimiter(a, b, c)`

Returns perimiter of a triangle with sides `a`, `b` and `c`

```
> perimiter(1, 2, 3)
6
```

## Rectangle

### Area

`area(a, b)`

Returns area of a rectangle with sides `a` and `b`

```
> area(4, 3)
12
```

### Perimiter

`perimiter(a, b)`

Returns perimiter of a rectangle with sides `a` and `b`

```
> perimiter(7, 4)
22
```

## Circle

### Area

`area(r)`

Returns area of a circle with radius `r`

```
> area(2)
12.566370614359172
```

### Perimiter

`perimiter(r)`

Returns perimiter (circumference) of a circle with radius `r`

```
> perimiter(3)
18.84955592153876
```

## Square

### Area

`area(a)`

Returns area of a square with side `a`

```
> area(3)
9
```

### Perimiter

`perimiter(a)`

Returns perimiter of a square with side `a`

```
> perimiter(2)
8
```
