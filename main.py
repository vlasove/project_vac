import sqlite3
from cli.cli import CLI 

interface = CLI()
configs = interface.get_result()

print(configs)

conn = sqlite3.connect(configs['path'])
cur = conn.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS vacancys (id INT PRIMARY KEY, search TEXT, title TEXT, company TEXT, salary INT)'
cur.execute(create_table)

insert_query = 'INSERT INTO vacancys VALUES(NULL, ?, ?, ?, ?)'
for i in range(10):
    data = (configs['vacancy'], 'Python Developer', 'Comp' + str(i), 1000 + i*10)
    cur.execute(insert_query, data)

conn.commit()
conn.close()

