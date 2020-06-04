import requests
from bs4 import BeautifulSoup


class Parser:
    headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.142",
            "accept": "*/*"
        }

    def __init__(self, search:str):
        self.__base_url = "https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&only_with_salary=true&search_period=30&text=%s&page=0"%(search)
        self.__session = requests.Session()
        self.__vacancy_bag = []
        self.__converter = {"руб." : 1, "USD" : 72, "EUR" : 81}

    def get_vacancy_bag(self):
        return self.__vacancy_bag

    def __check_connection(self):
        if self.__session.get(self.__base_url, headers=self.headers).status_code == 200:
            return True 
        return False 

    def get_last_page(self):
        if self.__check_connection():
            soup = BeautifulSoup(self.__session.get(self.__base_url, headers=self.headers).content, "lxml")
            pages = soup.find_all('a', attrs={"data-qa":"pager-page"})
            return int(pages[-1].text) - 1

    def __parse_salary(self, salary:str):
        #120 000-200 000 руб.
        #1 000-1 600 USD
        words_list = salary.split() # ['120', '000-200', '000', 'руб.']
        try:
            first = int(words_list[0])
            second = int(words_list[1].split('-')[-1]) #['000', '200']
            avg = (first + second) / 2
            return int(avg) * 1000 * self.__converter[words_list[-1]] 

        except: 
            #от 110 000 руб.
            first = int(words_list[1])
            return first * 1000 * self.__converter[words_list[-1]]

    def get_vacancys(self):
        last_page = self.get_last_page()
        for page in range(0, last_page + 1):
            self.__base_url = self.__base_url[:-1] + str(page)

            if self.__check_connection():
                soup = BeautifulSoup(self.__session.get(self.__base_url, headers=self.headers).content, "lxml")
                vacancy_cards = soup.find_all("div", attrs={"data-qa": "vacancy-serp__vacancy"})

                for vac in vacancy_cards:
                    try:
                        title = vac.find("a", attrs={"data-qa" : "vacancy-serp__vacancy-title"}).text
                        company = vac.find("a", attrs = {"data-qa" : "vacancy-serp__vacancy-employer"}).text
                        salary = vac.find("span", attrs={"data-qa" : "vacancy-serp__vacancy-compensation"}).text 
                        if self.__parse_salary(salary) > 1000000:
                            pass 
                        else:
                            self.__vacancy_bag.append((title, company, self.__parse_salary(salary)))
                    except:
                        pass 









# base_url = "https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&only_with_salary=true&search_period=30&text=%s&page=%i"%("python", 0)

# session = requests.Session()
# req = session.get(base_url, headers=headers)
# if req.status_code == 200:
#     print("Connection successfull!")
#     #pip install lxml
#     soup = BeautifulSoup(req.content, "lxml")
#     vacancy_cards = soup.find_all("div", attrs={"data-qa": "vacancy-serp__vacancy"})

#     for vac in vacancy_cards:
#         try:
#             title = vac.find("a", attrs={"data-qa" : "vacancy-serp__vacancy-title"}).text
#             company = vac.find("a", attrs = {"data-qa" : "vacancy-serp__vacancy-employer"}).text
#             salary = vac.find("span", attrs={"data-qa" : "vacancy-serp__vacancy-compensation"}).text 
#             print(title, company, salary)
#         except:
#             pass 
        

# else:
#     print("Connection error happend")

