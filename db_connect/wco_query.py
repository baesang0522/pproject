from pproject.db_connect.db_connection import hive
import pandas as pd


def article_query():
    query = """
            select country
                 , content
              from bigdata.dz_bdp_news_001m
             where content != 'Not Found'
            """
    with hive() as conn:
        article_dataframe = pd.read_sql(query, conn)

    return article_dataframe





