import os
import psycopg2



def db_connect():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=os.environ.get("DB_PORT", 5432)
    )


def create_table():
    conn=db_connect()
    cursor=conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        email VARCHAR(150) PRIMARY KEY,
        fullname VARCHAR(100),
        password VARCHAR(255)
    )""")

    conn.commit()
    conn.close()
