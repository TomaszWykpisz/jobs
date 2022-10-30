from scraper import Scraper
from bs4 import BeautifulSoup

class Pracuj():

    def __init__(self):

        self.domain = "https://www.pracuj.pl"
        self.jobs = {}
        print("PRACUJ INIT")


    def get_data_from_website(self):

        i = 1
        while True:

            url = self.domain + "/praca/poznan;wp?rd=5&pn=" + str(i)
            class_check = "app-banner__search-box"
            
            response = Scraper().openUrl(url, class_check)
            if response:
                i += 1
                self.get_job_offers(response)
            else:
                break


    def get_job_offers(self, html):

        bs = BeautifulSoup(html, 'html.parser')

        list = bs.find_all(attrs={"class": "results__list-container-item"})    

        for li in list:
            a = li.find(attrs={"class": "offer-details__title-link"})
            if a:
                self.jobs[a['href']] = a.get_text()

    def show_data(self):

        for job in self.jobs:
            print(f"{job} :: {self.jobs[job]}")

