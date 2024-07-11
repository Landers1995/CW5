from course_work_5.api_clients import HeadHunterAPIClient
from course_work_5.config import settings
from course_work_5.db.loader import load_employers, load_vacancies
from course_work_5.db.managers import PostgresDBManager
from course_work_5.db.migrations import create_database, apply_migrations
from course_work_5.user_interaction import print_employers, run_interation


def main():
    """Скрипт, активирующий программу"""

    print('Создание схем...')

    create_database()
    apply_migrations()

    load_employers()
    load_vacancies()

    run_interation()


if __name__ == '__main__':
    main()
