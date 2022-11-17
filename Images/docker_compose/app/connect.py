import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    connection = None
    try:
        # read connection parameters
        params = config()

        while connection == None:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            connection = psycopg2.connect(**params)

        print("Connection established.")
        # create a cursor
        cursor = connection.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cursor.fetchone()
        print(db_version)

        return connection, cursor
        # cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #    if conn is not None:
    #        conn.close()
    #        print('Database connection closed.')


def closing(conn, cursor):
    if cursor is not None:
        cursor.close()

    if conn is not None:
        conn.close()
        print('Database connection closed.')


if __name__ == '__main__':
    connect()
