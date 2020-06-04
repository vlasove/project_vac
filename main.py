import sqlite3
from cli.cli import CLI 
from model.vacancy import VacancyAnalyser
from model.vacancy import Vacancy
from model.create_table import create_table



interface = CLI()
configs = interface.get_result()

create_table(configs['path'])

v1 = Vacancy(configs['path'], configs['vacancy'], "Python Developer2", "Avito2", 150000)
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


