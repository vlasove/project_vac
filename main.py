import sqlite3
from cli.cli import CLI 
from model.vacancy import VacancyAnalyser
from model.vacancy import Vacancy



interface = CLI()
configs = interface.get_result()

vac = VacancyAnalyser(configs['path'], configs['vacancy'], configs['avg'], configs['std'])

for elem in vac.show_total():
    print(elem)

if configs["avg"] and configs["std"]:   
    print("Average Salary:", int(vac.average()), "STD of Salary:", int(vac.std()))
elif configs["avg"] and configs["std"] == False:
    print("Average Salary:", int(vac.average()))
elif configs["std"] and configs["avg"] == False:
    print("STD of Salary:", int(vac.std()))
else: 
    pass 


