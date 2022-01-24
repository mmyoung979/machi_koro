# Third party imports
from psycopg2 import connect

# Local imports
from apis.utils.logging_utils import get_logger
from settings import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

# Global variables
LOGGER = get_logger()


def make_connection():
    return connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def query_database(sql):
    with make_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
    LOGGER.info(f"Executed SQL:\n{sql}")
    return results


def update_database(sql):
    LOGGER.info(f"Executing SQL:\n{sql}")
    with make_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
