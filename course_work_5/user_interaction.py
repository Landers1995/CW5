from course_work_5.db.managers import PostgresDBManager
from prettytable import PrettyTable


def print_employers():
    db_manager = PostgresDBManager()
    try:
        res = db_manager.get_companies_and_vacancies_count()
    finally:
        db_manager.disconnect()
    table = PrettyTable(field_names=['Название компаний', 'Количество вакансий'])
    for data in res:
        table.add_row([data[0], data[1]])
    print(table)


def print_average_salary():
    db_manager = PostgresDBManager()
    try:
        salary = db_manager.get_avg_salary()
    finally:
        db_manager.disconnect()
    print(f'Средняя зарплата: {salary} рублей')


def run_interation():
    user_actions = {
        '1': print_employers,
        '2': print_average_salary
    }
    while True:
        print(
            'Выберете что сделать:',
            '1 - получить список всех компаний и количество вакансий у каждой компании',
            '2 - получить среднюю зарплату по вакансиям',
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
