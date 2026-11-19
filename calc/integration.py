"""Подынтегральные функции и метод левых прямоугольников."""

import math

MAX_STEPS = 100_000


def ratio(x):
    """Вычислить x / (x + 1)."""
    return x / (x + 1)


def root(x):
    """Вычислить квадратный корень из x² + 1."""
    return math.sqrt(x * x + 1)


FUNCTIONS = {
    "ratio": (ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}


def validate_limits(start, end, low, high, with_ends):
    """Проверить порядок, конечность и принадлежность пределов промежутку."""
    if not math.isfinite(start) or not math.isfinite(end):
        raise ValueError("пределы интегрирования должны быть конечными")
    if start >= end:
        raise ValueError("начальный предел не меньше конечного")
    if with_ends:
        inside = low <= start < end <= high
    else:
        inside = low < start < end < high
    if not inside:
        raise ValueError("предел вне промежутка")


def integrate(f, start, end, steps):
    """Вычислить интеграл методом левых прямоугольников."""
    if not 1 <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")
    dx = (end - start) / steps
    result = 0.0
    for i in range(steps):
        result += f(start + i * dx) * dx
    return result
