from scraper import Scraper
from bs4 import BeautifulSoup

class Olx():

    def __init__(self):

        self.domain = "https://www.olx.pl"
        self.jobs = {}


    def get_data_from_website(self):

        i = 1
        while True:
            url = self.domain + "/d/praca/poznan/?search%5Border%5D=created_at%3Adesc&page=" + str(i)
            class_check = "listing-grid-container"
            
            response = Scraper().open_url_selenium(url, class_check)
            if response:
                i += 1
                if not self.get_job_offers(response): break
            else:
                break


    def get_job_offers(self, html):

        bs = BeautifulSoup(html, 'html.parser')
        list = bs.find_all(attrs={"class": "css-19ucd76"})    

        new_job_counter = 0
        for li in list:
            a = li.find("a")
            if a:

                href = self.domain + a['href']
                if not href in self.jobs:

                    print(href)
                    new_job_counter += 1
                    
                    text = li.find("h6").get_text()
                    self.jobs[href] = text

        return new_job_counter


    def show_data(self):

        for job in self.jobs:
            print(f"{job} :: {self.jobs[job]}")

