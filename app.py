import sqlite3
from cli.cli import CLI 
from model.vacancy import VacancyAnalyser
from model.vacancy import Vacancy
from model.create_table import create_table
from connector.connector import Parser

from tqdm import tqdm



interface = CLI()
configs = interface.get_result()

create_table(configs['path'])

p = Parser(configs["vacancy"])
p.get_vacancys()
for vac in tqdm(p.get_vacancy_bag()):
    v1 = Vacancy(configs['path'], configs['vacancy'], vac[0], vac[1], vac[2])
    v1.save()



vac = VacancyAnalyser(configs['path'], configs['vacancy'], configs['avg'], configs['std'])

for elem in vac.show_total():
    print(elem)

if configs["avg"] and configs["std"]:   
    print("Average Salary:", int(vac.average()), "rub.",  "STD of Salary:", int(vac.std()), "rub.")
elif configs["avg"] and configs["std"] == False:
    print("Average Salary:", int(vac.average()), "rub.")
elif configs["std"] and configs["avg"] == False:
    print("STD of Salary:", int(vac.std()), "rub.")
else: 
    pass 


