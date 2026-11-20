# Python OOP: Modular Analytics & Reporting Pipeline

[English](#english) | [Русский](#русский)

---

## English

A progressive implementation of Object-Oriented Programming (OOP) principles in **Python 3**. The project evolves from basic class definitions to a modular, configurable analytics and reporting pipeline featuring input validation, inheritance, structured logging, and Telegram webhook notifications.

###  Tech Stack & Architecture
* **Language:** Python 3 (standard library: `sys`, `os`, `random`, `logging`, `json`, `urllib` / `requests`)
* **Design Principles:** Encapsulation, composition (nested classes), inheritance, separation of configuration and business logic, structured file logging.

###  Project Structure (`src/`)

* **`ex00/first_class.py`** — Basic class definition (`Must_Read`) for reading and displaying CSV data.
* **`ex01/first_method.py`** — Encapsulating file reading logic inside the `file_reader()` method of the `Research` class.
* **`ex02/first_constructor.py`** — Adding `__init__()` constructor for dynamic file path handling via CLI arguments and strict CSV structure validation with exception handling.
* **`ex03/first_nest.py`** — Parsing CSV rows into integer lists (`has_header` flag) and introducing a nested `Calculations` class (`counts()` and `fractions()`).
* **`ex04/first_child.py`** — Implementing inheritance: `Analytics` inherits from `Calculations` and adds `predict_random()` and `predict_last()` methods.
* **`ex05/config.py`, `analytics.py`, `make_report.py`** — Refactoring into a modular architecture: moving parameters and text templates into `config.py`, adding file export (`save_file()`), and generating analytical reports via `make_report.py`.
* **`ex06/config.py`, `analytics.py`, `make_report.py`** — Production readiness: adding timestamped debug logging (`analytics.log`) across all class methods and sending report status notifications to Telegram via webhooks.

###  Usage Example
* Run constructor & validation script: `python3 src/ex02/first_constructor.py data.csv`
* Generate analytical report with logging: `python3 src/ex06/make_report.py`

---

## Русский

Последовательная реализация принципов объектно-ориентированного программирования (ООП) на **Python 3**. Проект развивается от базового объявления классов до модульного конвейера аналитики и генерации отчётов с валидацией входных данных, наследованием, логированием и отправкой уведомлений через Telegram-вебхуки.

###  Стек и архитектурные принципы
* **Язык:** Python 3 (стандартная библиотека: `sys`, `os`, `random`, `logging`, `json`, `urllib` / `requests`)
* **Принципы проектирования:** Инкапсуляция, композиция (вложенные классы), наследование, разделение конфигурации и бизнес-логики, логирование этапов выполнения.

###  Структура проекта (`src/`)

* **`ex00/first_class.py`** — Базовый класс `Must_Read` для чтения и вывода содержимого CSV-файла.
* **`ex01/first_method.py`** — Вынос логики чтения файла в метод `file_reader()` класса `Research`.
* **`ex02/first_constructor.py`** — Добавление конструктора `__init__()` для передачи пути к файлу через аргументы командной строки и строгой валидации структуры CSV с выбросом исключений.
* **`ex03/first_nest.py`** — Преобразование строк файла в список списков целых чисел (с параметром `has_header`) и реализация вложенного класса `Calculations` (`counts()` и `fractions()`).
* **`ex04/first_child.py`** — Реализация наследования: класс `Analytics` наследуется от `Calculations` и расширяет его методами прогнозирования `predict_random()` и `predict_last()`.
* **`ex05/config.py`, `analytics.py`, `make_report.py`** — Модульный рефакторинг: вынос параметров и шаблонов текста в `config.py`, добавление сохранения результатов в файл (`save_file()`) и генерация итогового отчёта в `make_report.py`.
* **`ex06/config.py`, `analytics.py`, `make_report.py`** — Подготовка к продакшену: добавление детального логирования всех методов в файл `analytics.log` и отправка статуса формирования отчёта в Telegram-канал через webhook.

###  Примеры запуска
* Запуск скрипта с валидацией входного файла: `python3 src/ex02/first_constructor.py data.csv`
* Генерация итогового отчёта с логированием: `python3 src/ex06/make_report.py`
