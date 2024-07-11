from course_work_5.db.managers import PostgresDBManager
from prettytable import PrettyTable


def print_employers():
    """Вывод информации о работодателях и количества предлагаемых ими вакансий"""

    db_manager = PostgresDBManager()
    try:
        res = db_manager.get_companies_and_vacancies_count()
    finally:
        db_manager.disconnect()
    table = PrettyTable(field_names=['Название компаний', 'Количество вакансий'])
    for data in res:
        table.add_row([data[0], data[1]])
    print(table)


def print_get_all_vacancies():
    """Вывод информации о всех вакансиях"""

    db_manager = PostgresDBManager()
    try:
        res = db_manager.get_all_vacancies()
    finally:
        db_manager.disconnect()
    table = PrettyTable(field_names=['Название компаний', 'Название вакансий', 'Зарплато от', 'Заплата до', 'Ссылка на вакансию'])
    for data in res:
        table.add_row([data[0], data[1], data[2], data[3], data[4]])
    print(table)


def print_average_salary():
    """Вывод информации о средней зарплате среди всех вакансий"""

    db_manager = PostgresDBManager()
    try:
        salary = db_manager.get_avg_salary()
    finally:
        db_manager.disconnect()
    print(f'Средняя зарплата: {salary} рублей')


def print_get_vacancies_with_higher_salary():
    """Вывод информации о зарплатах, превышающей среднюю зарплату"""

    db_manager = PostgresDBManager()
    try:
        res = db_manager.get_vacancies_with_higher_salary()
    finally:
        db_manager.disconnect()
    table = PrettyTable(field_names=['Название компаний', 'Название вакансий', 'Зарплата от', 'Зарплата до', 'Ссылка на вакансию'])
    for data in res:
        table.add_row([data[0], data[1], data[2], data[3], data[4]])
    print(table)


def print_get_vacancies_with_keyword():
    """Вывод информации о вакансиях по ключевому слову"""

    db_manager = PostgresDBManager()
    try:
        res = db_manager.get_vacancies_with_keyword()
    finally:
        db_manager.disconnect()
    table = PrettyTable(field_names=['Название компаний', 'Название вакансий', 'Зарплата от', 'Зарплата до', 'Ссылка на вакансию'])
    for data in res:
        table.add_row([data[0], data[1], data[2], data[3], data[4]])
    print(table)


def run_interation():
    """Интерфейс для управления программой"""

    user_actions = {
        '1': print_employers,
        '2': print_average_salary,
        '3': print_get_all_vacancies,
        '4': print_get_vacancies_with_higher_salary,
        '5': print_get_vacancies_with_keyword,
    }
    while True:
        print(
            'Выберете что сделать:',
            '1 - получить список всех компаний и количество вакансий у каждой компании',
            '2 - получить среднюю зарплату по вакансиям',
            '3 - получить список всех вакансий',
            '4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям',
            '5 - получить список всех вакансий, в названии которых содержатся переданные в метод слова',
            '0 - выйти',
            sep='\n'
        )
        user_input = input()

        if user_input == '0':
            break
        elif user_input in user_actions:
            handler = user_actions[user_input]
            handler()

        print()
