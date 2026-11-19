# Mathtool

Консольное приложение для лабораторных работ № 1 и № 2. Требуется Python 3.12 или новее. Все команды выполняются из папки проекта.

```powershell
python mathtool.py --help
python mathtool.py solve -a 1 -b -3 -c 2
python mathtool.py stats --input numbers.txt
"4 1 5" | python mathtool.py stats
python mathtool.py series --func sqplus --eps 0.0001
python mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000
```

Команда `solve` без коэффициентов запрашивает их по очереди. Для ручного ввода в `stats` введите числа через пробел или на отдельных строках. Чтобы закончить ввод в Windows, нажмите Ctrl+Z, затем Enter.

У каждой команды есть собственная справка, например `python mathtool.py integrate --help`. Справка и результаты идут в stdout, ошибки — в stderr. Код возврата равен 0 при успехе, 1 при ошибке данных и 2 при ошибке разбора аргументов. В PowerShell код можно посмотреть командой `$LASTEXITCODE` сразу после запуска.

`mathtool.py` отвечает за запуск и вывод, `cli.py` описывает команды, а пакет `calc` выполняет расчёты. В `tests.txt` записаны команды проверки, входные данные и ожидаемые результаты.
