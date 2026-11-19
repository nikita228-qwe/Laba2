"""Проверка последовательности и вычисление её показателей."""

import math

MAX_COUNT = 20
MAX_ABS = 10_000


def validate(numbers):
    """Проверить количество, конечность и диапазон чисел."""
    if not numbers:
        raise ValueError("последовательность пуста")
    if len(numbers) > MAX_COUNT:
        raise ValueError(f"чисел больше {MAX_COUNT}")
    for number in numbers:
        if not math.isfinite(number):
            raise ValueError("все числа должны быть конечными")
        if abs(number) > MAX_ABS:
            raise ValueError("значение вне допустимого диапазона")


def total(numbers):
    """Вернуть сумму чисел."""
    return math.fsum(numbers)


def mean(numbers):
    """Вернуть среднее арифметическое."""
    return total(numbers) / len(numbers)


def square_sum(numbers):
    """Вернуть сумму квадратов."""
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return math.fsum(squares)


def rms(numbers):
    """Вернуть среднее квадратическое."""
    return math.sqrt(square_sum(numbers) / len(numbers))


def squared_deviations(numbers):
    """Вернуть сумму квадратов отклонений от среднего."""
    average = mean(numbers)
    squares = []
    for number in numbers:
        squares.append((number - average) ** 2)
    return math.fsum(squares)


def variance(numbers):
    """Вернуть дисперсию с делением на N."""
    return squared_deviations(numbers) / len(numbers)


def population_stddev(numbers):
    """Вернуть корень из дисперсии с делением на N."""
    return math.sqrt(variance(numbers))


def sample_stddev(numbers):
    """Вернуть отклонение по N − 1 или None для одного числа."""
    if len(numbers) == 1:
        return None
    return math.sqrt(squared_deviations(numbers) / (len(numbers) - 1))


def minimum(numbers):
    """Вернуть наименьшее число."""
    return min(numbers)


def maximum(numbers):
    """Вернуть наибольшее число."""
    return max(numbers)


def positive_count(numbers):
    """Посчитать строго положительные числа."""
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count


def negative_count(numbers):
    """Посчитать строго отрицательные числа."""
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return count


REPORT = (
    ("Количество", len, "d"),
    ("Сумма", total, ".3f"),
    ("Ср. арифм.", mean, ".3f"),
    ("Сумма кв.", square_sum, ".3f"),
    ("Ср. кв.", rms, ".3f"),
    ("Дисперсия", variance, ".3f"),
    ("СКО", population_stddev, ".3f"),
    ("Станд. откл.", sample_stddev, ".3f"),
    ("Наименьшее", minimum, ".3f"),
    ("Наибольшее", maximum, ".3f"),
    ("Положительных", positive_count, "d"),
    ("Отрицательных", negative_count, "d"),
)
