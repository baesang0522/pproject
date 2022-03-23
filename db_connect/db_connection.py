from pproject.db_connect import Config
import pyodbc


def hive():
    conn = pyodbc.connect(f'DSN={Config.db_dsn}', autocommit=True)
    return conn
