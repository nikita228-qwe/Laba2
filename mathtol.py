import sys
from calc import equation
def main():
    try:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
        yr, D , x = equation.solve(a, b, c) 
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        return 1
print(f"Тип уравнения: {yr}")
if yr == "Линейное":
    print ("D: нет")
if yr == "Квадратное" and D == "D=0":
    print ("D: 0")
    print (f"Корень: {x[0]}")
if yr == "Квадратное" and D != "D=0":
    print (f"D: {D}")
    print (f"Корни: {x[0]} и {x[1]}")
main()