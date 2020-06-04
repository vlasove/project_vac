import sqlite3
from cli.cli import CLI 
from model.vacancy import VacancyAnalyser

interface = CLI()
configs = interface.get_result()

vac = VacancyAnalyser(configs['path'], configs['vacancy'], configs['avg'], configs['std'])

for elem in vac.show_total():
    print(elem)
#print(vac.average(), vac.std())

# print(configs)

# conn = sqlite3.connect(configs['path'])
# cur = conn.cursor()

# create_table = 'CREATE TABLE IF NOT EXISTS vacancys (id INTEGER PRIMARY KEY, search TEXT, title TEXT, company TEXT, salary INT)'
# cur.execute(create_table)

# insert_query = 'INSERT INTO vacancys VALUES(NULL, ?, ?, ?, ?)'
# for i in range(10):
#     data = (configs['vacancy'], 'Java Developer', 'Comp' + str(i), 10000 + i*10)
#     cur.execute(insert_query, data)

# conn.commit()
# conn.close()

