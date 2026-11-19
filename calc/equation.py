"""Проверка коэффициентов и решение уравнения."""

import math

MAX_VALUE = 10_000


def validate_coefficients(numbers):
    """Проверить диапазон коэффициентов и наличие неизвестного."""
    for name, number in numbers.items():
        if abs(number) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")
    if numbers["A"] == numbers["B"] == 0:
        raise ValueError("это не уравнение, неизвестное отсутствует")


def solve(a, b, c):
    """Вернуть вид уравнения, дискриминант и действительные корни."""
    validate_coefficients({"A": a, "B": b, "C": c})
    if a == 0:
        return "линейное", None, [-c / b + 0.0]

    d = b * b - 4 * a * c
    if d < 0:
        return "квадратное", d, []
    if d == 0:
        return "квадратное", d, [-b / (2 * a) + 0.0]

    root = math.sqrt(d)
    return "квадратное", d, [
        (-b + root) / (2 * a) + 0.0,
        (-b - root) / (2 * a) + 0.0,
    ]
