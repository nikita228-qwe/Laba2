"""Точка входа mathtool, получение данных и вывод результатов."""

import sys

from calc import equation, integration, series, stats
from cli import build_parser


def handle_solve(args):
    """Получить коэффициенты, решить уравнение и напечатать ответ."""
    a, b, c = args.a, args.b, args.c
    if a is None and b is None and c is None:
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except (ValueError, EOFError) as error:
            raise ValueError("коэффициент не является целым числом") from error
    elif None in (a, b, c):
        raise ValueError("укажите все три коэффициента либо ни одного")

    equation_type, d, roots = equation.solve(a, b, c)
    print(f"Уравнение {equation_type}")
    if d is not None:
        print(f"Дискриминант: {d}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif roots:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")
    return 0


def read_numbers(lines):
    """Прочитать вещественные числа из строк файла или стандартного ввода."""
    numbers = []
    for line in lines:
        for word in line.split():
            try:
                numbers.append(float(word))
            except ValueError as error:
                raise ValueError(f"{word} не является числом") from error
            if len(numbers) > stats.MAX_COUNT:
                raise ValueError(f"чисел больше {stats.MAX_COUNT}")
    return numbers


def handle_stats(args):
    """Прочитать последовательность и напечатать все показатели."""
    if args.input is None:
        numbers = read_numbers(sys.stdin)
    else:
        try:
            with open(args.input, encoding="utf-8-sig") as lines:
                numbers = read_numbers(lines)
        except OSError as error:
            raise OSError("файл не открывается") from error

    stats.validate(numbers)
    for name, func, fmt in stats.REPORT:
        number = func(numbers)
        if number is None:
            answer = "НЕ СУЩЕСТВУЕТ"
        else:
            answer = format(number, fmt)
        print(f"{name}: {answer}")
    return 0


def handle_series(args):
    """Просуммировать выбранный ряд и напечатать число слагаемых."""
    term, formula = series.FORMULAS[args.func]
    if args.terms is not None:
        count = args.terms
        result = series.sum_by_terms(term, count)
    else:
        result, count = series.sum_by_eps(term, args.eps)

    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {result:.4f}")
    return 0


def handle_integrate(args):
    """Проверить пределы, вычислить интеграл и напечатать результат."""
    func, formula, low, high, with_ends = integration.FUNCTIONS[args.func]
    integration.validate_limits(args.start, args.end, low, high, with_ends)
    result = integration.integrate(func, args.start, args.end, args.steps)
    print(formula)
    print(f"Значение интеграла: {result:.4f}")
    return 0


HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}


parser = build_parser()
args = parser.parse_args()

if args.command is None:
    parser.print_help()
else:
    try:
        HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        sys.exit(1)
