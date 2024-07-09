from pathlib import Path

from course_work_5.config import settings
from course_work_5.db.managers import PostgresDBManager


def create_database():
    db_manager = PostgresDBManager(db_name='postgres')
    db_manager.connect()
    db_manager.connection.autocommit = True

    try:
        with db_manager.connection.cursor() as cursor:
            cursor.execute(f'drop database if exists {settings.DB_NAME}')
            cursor.execute(f'create database {settings.DB_NAME}')

        db_manager.commit()

    finally:
        db_manager.disconnect()


def apply_migrations():
    db_manager = PostgresDBManager()
    db_manager.connect()

    try:
        with db_manager.connection.cursor() as cursor:
            for migration in sorted(settings.MIGRATIONS_DIR.glob('*.sql')):
                cursor.execute(_read_migrations(migration))

            db_manager.commit()
    finally:
        db_manager.disconnect()


def _read_migrations(file_path: Path) -> str:
    with file_path.open(encoding='utf-8') as f:
        return f.read()


