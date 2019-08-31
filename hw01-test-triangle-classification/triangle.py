def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise AttributeError('Each triangle side must be a positive value.')

    a2 = a ** 2
    b2 = b ** 2
    c2 = c ** 2

    if a2 + b2 == c2 or b2 + c2 == a2 or a2 + c2 == b2:
        return 'right'
    if a == b:
        return 'equilateral' if b == c else 'isosceles'
    return 'isosceles' if b == c or a == c else 'scalene'
