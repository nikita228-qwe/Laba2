"""Описание команд и параметров mathtool."""

import argparse

from calc import equation, integration, series, stats


def build_parser():
    """Создать разборщик с общей справкой и справкой каждой команды."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="Расчёты над уравнениями и числовыми последовательностями.",
        allow_abbrev=False,
    )
    commands = parser.add_subparsers(dest="command")

    solve = commands.add_parser(
        "solve", help="решить линейное или квадратное уравнение",
        description="Укажите все три коэффициента либо введите их с клавиатуры.",
        allow_abbrev=False,
    )
    for name in "abc":
        solve.add_argument(
            f"-{name}", type=int,
            help=f"целый коэффициент {name.upper()} по модулю до {equation.MAX_VALUE}",
        )

    stats_parser = commands.add_parser(
        "stats", help="вычислить показатели последовательности",
        description=f"Статистика по последовательности из 1–{stats.MAX_COUNT} чисел.",
        allow_abbrev=False,
    )
    stats_parser.add_argument("--input", help="файл с числами, по умолчанию стандартный ввод")

    series_parser = commands.add_parser(
        "series", help="просуммировать знакочередующийся ряд",
        description="Сложить ряд по количеству слагаемых или по точности.",
        allow_abbrev=False,
    )
    series_parser.add_argument("--func", choices=sorted(series.FORMULAS), required=True,
                           help="имя ряда")
    group = series_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int,
                      help=f"количество слагаемых от 1 до {series.MAX_TERMS}")
    group.add_argument("--eps", type=float, help=f"точность, 0 < eps <= {series.MAX_EPS}")

    integrate_parser = commands.add_parser(
        "integrate", help="вычислить интеграл методом левых прямоугольников",
        description="Интеграл на заданном отрезке.",
        allow_abbrev=False,
    )
    integrate_parser.add_argument("--func", choices=sorted(integration.FUNCTIONS), required=True,
                          help="функция: ratio на [0; 20], root на (-5; 5)")
    integrate_parser.add_argument("--from", dest="start", type=float, required=True,
                          help="нижний предел интегрирования")
    integrate_parser.add_argument("--to", dest="end", type=float, required=True,
                          help="верхний предел интегрирования")
    integrate_parser.add_argument("--steps", type=int, required=True,
                          help=f"количество шагов от 1 до {integration.MAX_STEPS}")
    return parser
