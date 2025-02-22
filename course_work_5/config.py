import json
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


class Settings:
    """Класс подключения к базе данных"""

    DB_NAME = 'hw5'
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    EMPLOYEE_IDS_CONFIG_PATH = BASE_DIR.joinpath('employers_config.json')
    MIGRATIONS_DIR = BASE_DIR.joinpath('course_work_5', 'migrations')

    def get_employer_ids(self) -> list[int]:
        """Получение id работодателей"""

        with self.EMPLOYEE_IDS_CONFIG_PATH.open() as f:
            data = json.load(f)

        return data['employers']['hh']


settings = Settings()

