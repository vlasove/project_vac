import sqlite3
from cli.cli import CLI 
from model.vacancy import VacancyAnalyser
from model.vacancy import Vacancy

interface = CLI()
configs = interface.get_result()

v1 = Vacancy("php", "Laravel Developer", "VK.com", 150000)
v1.save()

v1.delete()

vac = VacancyAnalyser(configs['path'], configs['vacancy'], configs['avg'], configs['std'])

for elem in vac.show_total():
    print(elem)
print("Average Salary:", int(vac.average()), "STD of Salary:", int(vac.std()))


