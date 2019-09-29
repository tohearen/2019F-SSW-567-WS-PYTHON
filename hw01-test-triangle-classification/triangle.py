"""Triangle classification"""


def classify_triangle(line_a, line_b, line_c):
    """Return the type of triangle based on the length of its lines"""
    if line_a <= 0 or line_b <= 0 or line_c <= 0:
        raise AttributeError('Each triangle side must be a positive value.')

    a_sq = line_a ** 2
    b_sq = line_b ** 2
    c_sq = line_c ** 2

    if a_sq + b_sq == c_sq or b_sq + c_sq == a_sq or a_sq + c_sq == b_sq:
        return 'right'
    if line_a == line_b:
        return 'equilateral' if line_b == line_c else 'isosceles'
    return 'isosceles' if line_c in (line_a, line_b) else 'scalene'
