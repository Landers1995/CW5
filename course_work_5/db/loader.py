from tqdm import tqdm

from course_work_5.api_clients import HeadHunterAPIClient
from course_work_5.config import settings
from course_work_5.db.managers import PostgresDBManager

api_client = HeadHunterAPIClient()


def load_employers():
    """Загрузка списка работодателей в базу данных"""

    employer_ids = settings.get_employer_ids()
    sql = """
        INSERT INTO employers(id, name, url, site_url, region)
        VALUES(%s, %s, %s, %s, %s);
        """
    db_manager = PostgresDBManager()
    db_manager.connect()

    try:
        with db_manager.connection.cursor() as cursor:
            for employer_id in tqdm(employer_ids, desc='Загрузка работодателей...'):
                emp = api_client.get_employer_info(employer_id)
                cursor.execute(sql, (emp.id, emp.name, emp.url, emp.site_url, emp.region))

            db_manager.commit()
    finally:
        db_manager.disconnect()


def load_vacancies():
    """Загрузка списка вакансий в базу данных"""

    employer_ids = settings.get_employer_ids()
    sql = """
        INSERT INTO vacancies(id, name, url, type, salary_from, salary_to, employer_id)
        VALUES(%s, %s, %s, %s, %s, %s, %s);
        """
    db_manager = PostgresDBManager()
    db_manager.connect()

    try:
        with db_manager.connection.cursor() as cursor:
            for employer_id in tqdm(employer_ids, desc='Загрузка вакансий...'):
                vacancies = api_client.get_employer_vacancies(employer_id)
                data = (
                    (vac.id, vac.name, vac.url, vac.type.name, vac.salary_from, vac.salary_to, employer_id)
                    for vac in vacancies
                )
                cursor.executemany(sql, data)

            db_manager.commit()
    finally:
        db_manager.disconnect()


