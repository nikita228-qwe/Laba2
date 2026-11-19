"""Формулы рядов и алгоритмы их суммирования."""

import math

MAX_TERMS = 10_000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100_000


def sqplus(n):
    """Вычислить n-е слагаемое ряда sqplus."""
    number = 1 / (n * n + 1)
    if n % 2 == 0:
        number = -number
    return number


def third(n):
    """Вычислить n-е слагаемое ряда third."""
    number = 1 / (3 * n)
    if n % 2 == 0:
        number = -number
    return number


FORMULAS = {
    "sqplus": (sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third": (third, "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
}


def sum_by_terms(term, count):
    """Сложить заданное число слагаемых."""
    if not 1 <= count <= MAX_TERMS:
        raise ValueError("количество слагаемых вне диапазона")
    result = 0.0
    for n in range(1, count + 1):
        result += term(n)
    return result


def sum_by_eps(term, eps):
    """Включить первое слагаемое с модулем меньше eps и остановиться."""
    if not math.isfinite(eps) or not 0 < eps <= MAX_EPS:
        raise ValueError("точность вне диапазона")
    result = 0.0
    for n in range(1, MAX_ITERATIONS + 1):
        number = term(n)
        result += number
        if abs(number) < eps:
            return result, n
    raise ValueError("точность не достигнута")
