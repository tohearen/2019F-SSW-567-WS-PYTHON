import pytest

import triangle


@pytest.mark.parametrize(
    "a, b, c, result",
    [
        (10, 24, 26, 'right'),
        (24, 26, 10, 'right'),
        (26, 10, 24, 'right'),
        (204, 253, 325, 'right'),
        (11, 61, 60, 'right'),
        (1, 1, 1, 'equilateral'),
        (2, 2, 2, 'equilateral'),
        (1000, 1000, 1000, 'equilateral'),
        (2, 2, 3, 'isosceles'),
        (3, 2, 2, 'isosceles'),
        (2, 3, 2, 'isosceles'),
        (9, 10000, 10000, 'isosceles'),
        (1, 2, 3, 'scalene'),
        (3, 2, 1, 'scalene'),
        (111, 222, 333, 'scalene'),
        (9, 20, 77, 'scalene'),
    ],
)
def test_classification(a, b, c, result):
    assert triangle.classify_triangle(a, b, c) == result


@pytest.mark.parametrize(
    "a, b, c",
    [
        (-1, 1, 2),
        (0, 0, 0),
        (2, 2, 0),
        (-2, 2, -100),
        (100, 77, 0),
        (100, 77, -1),
        (-4, -4, -1),
        (-1, 0, 1),
    ],
)
def test_attribute_error(a, b, c):
    with pytest.raises(AttributeError):
        triangle.classify_triangle(a, b, c)
