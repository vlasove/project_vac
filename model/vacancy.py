import sqlite3 

class VacancyAnalyser:
    def __init__(self, path:str, vacancy:str, calc_avg:bool, calc_std:bool):
        self.__path = path 
        self.__vacancy = vacancy 
        self.__calc_avg = calc_avg 
        self.__calc_std = calc_std

        self.__amount = 0
        self.__min = -1
        self.__max = -1
        self.__avg = 0
        self.__std = 0

        self.__answer_list = []

    def show_total(self):
        conn = sqlite3.connect(self.__path)
        cur = conn.cursor()

        select_query = 'SELECT salary FROM vacancys WHERE search = ?'
        vacancy_list = [] 
        for v in cur.execute(select_query, (self.__vacancy,)): # min([(1000), (1010), (1030), (1040)])[0] -> (1000)[0] -> 1000
            vacancy_list.append(v)


        self.__amount = len(vacancy_list)
        self.__min = min(vacancy_list)[0]
        self.__max = max(vacancy_list)[0]

        conn.close()

        self.__answer_list.append("Vacancys : %s in Moscow --- %i"%(self.__vacancy, self.__amount) )
        self.__answer_list.append("Min Salary: %i rub."%(self.__min))
        self.__answer_list.append("Max Salary: %i rub."%(self.__max))
            
        return self.__answer_list


    def average(self):
        conn = sqlite3.connect(self.__path)
        cur = conn.cursor()

        select_query = 'SELECT salary FROM vacancys WHERE search = ?'
        vacancy_list = [] 
        for v in cur.execute(select_query, (self.__vacancy,)): 
            vacancy_list.append(v) 

        ### your code 

        return self.__avg

    def std(self):
        conn = sqlite3.connect(self.__path)
        cur = conn.cursor()

        select_query = 'SELECT salary FROM vacancys WHERE search = ?'
        vacancy_list = [] 
        for v in cur.execute(select_query, (self.__vacancy,)): 
            vacancy_list.append(v) 

        ### your code 

        return self.__std