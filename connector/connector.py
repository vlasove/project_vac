import requests
from bs4 import BeautifulSoup


headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.142",
            "accept": "*/*"
        }


base_url = "https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&only_with_salary=true&search_period=30&text=%s&page=%i"%("python", 0)

session = requests.Session()
req = session.get(base_url, headers=headers)
if req.status_code == 200:
    print("Connection successfull!")
    #pip install lxml
    soup = BeautifulSoup(req.content, "lxml")
    vacancy_cards = soup.find_all("div", attrs={"data-qa": "vacancy-serp__vacancy"})

    for vac in vacancy_cards:
        try:
            title = vac.find("a", attrs={"data-qa" : "vacancy-serp__vacancy-title"}).text
            company = vac.find("a", attrs = {"data-qa" : "vacancy-serp__vacancy-employer"}).text
            salary = vac.find("span", attrs={"data-qa" : "vacancy-serp__vacancy-compensation"}).text 
            print(title, company, salary)
        except:
            pass 
        

else:
    print("Connection error happend")

