# luxmus_test
Test task for Luxmus organisation

## Системные требования
Язык для формирования ETL процесса - Python 3.11.6
База данных - SQLite3 

## Используемые библиотеки
SQLAlchemy==1.4.44
pandas==1.5.3
jupyterlab==4.0.10
json5==0.9.14
requests==2.31.0

## Использование программы через Jupyter Lab
1. Необходимо установить последнюю версию Python и установить необходимые библиотеки, перечисленные в requirements.txt;
2. Открыть jupyter-lab и открыть main.ipynb, в котором хранится основной скрипт программы;
3. Запустить все необходимые ячейки, что делает каждая ячейка описано в описание к соответствующей ячейке.

## Использование программы через консоль
1. Необходимо установить последнюю версию Python и установить необходимые библиотеки, перечисленные в requirements.txt;
2. Через командную строку запустить скрипт main.py.

## Возможные усовершенствования данного ПО
1. Добавление распаралелленых процессов, которые ускорят обращение к API и как следствие, ускорят обработку данного скрипта (multiprocessing);
2. Использование более современной базы данных (использование sqlite3 было обусловленно необходимостью хранения данных в файле для того, чтобы в дальнейшем было удобно проверить результаты);
3. Дополнение витрины данных для дашборда информацией относительно общего количества персонажей из различного вида происхождений.

