# Python imports
import logging
from os import listdir
from pathlib import Path

# Third party imports
import psycopg2

# Local imports
from apis.utils.db_utils import make_connection


def init_db():
    # Get schema files
    filepath = str(Path(__file__).resolve().parent.parent) + "/schema/"
    files = listdir(filepath)

    # use schema to build database
    with make_connection() as connection:
        with connection.cursor() as cursor:
            for file_ in files:
                with open(filepath + file_) as schema_file:
                    # Get rid of any newlines and whitespaces
                    sql = [line.strip() for line in schema_file.readlines()]

                    # Ignore commented out lines
                    sql = [line for line in sql if not line.startswith("--")]

                    # Make sure text was entered
                    if sql:
                        # Combine into one line
                        sql = " ".join(sql)

                        # Run SQL
                        try:
                            cursor.execute(sql)
                        except psycopg2.Error as err:
                            logging.info(sql)
                            logging.error(err)
                            cursor.execute("ROLLBACK")


if __name__ == "__main__":
    init_db()
