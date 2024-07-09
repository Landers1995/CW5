import psycopg2

from course_work_5.db.managers.base import DBManager


class PostgresDBManager(DBManager):

    def connect(self) -> None:
        if self.connection is None:
            self.connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )

    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_companies_and_vacancies_count(self) -> list[tuple[str, list]]:
        sql = """
            SELECT e.name, COUNT(*) as vacancies_count
            FROM employers as e
            LEFT JOIN vacancies as v ON e.id = v.employer_id
            GROUP BY e.name;
        """
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_all_vacancies(self):
        sql = """
            SELECT e.name, v.name, v.salary_from, v.salary_to, v.url FROM employers AS e
            LEFT JOIN vacancies AS v ON e.id = v.employer_id;
            """
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_avg_salary(self) -> float:
        sql = """SELECT AVG(v.salary_from), AVG(v.salary_to) FROM vacancies as v;"""
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            min_salary, max_salary = cursor.fetchone()
            average_salary = (min_salary + max_salary) / 2
            return round(average_salary, 2)

    def get_vacancies_with_higher_salary(self):
        sql = """
        SELECT e.name, v.name, v.salary_from, v.salary_to, v.url FROM employers AS e
        LEFT JOIN vacancies AS v ON e.id = v.employer_id
        where v.salary_to > %s
        order by v.salary_to;
            """
        res = self.get_avg_salary()
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (res,))
            return cursor.fetchall()

    def get_vacancies_with_keyword(self, text):
        #text = input('Введите     ')
        sql = """
        SELECT e.name, v.name, v.salary_from, v.salary_to, v.url FROM employers AS e
        LEFT JOIN vacancies AS v ON e.id = v.employer_id
        where v.name ilike '%python%'
        order by v.salary_to;
            """
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


