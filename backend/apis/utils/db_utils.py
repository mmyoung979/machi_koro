# Third party imports
from psycopg2 import connect

# Local imports
from settings import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


def make_connection():
    return connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def execute_sql(sql):
    with make_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

    return results
