import sqlite3 

def create_table(path:str):
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    query_create = 'CREATE TABLE IF NOT EXISTS vacancys (id INTEGER PRIMARY KEY,  search TEXT, title TEXT, company TEXT, salary INT)'
    cur.execute(query_create)

    conn.close()