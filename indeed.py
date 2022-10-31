from scraper import Scraper
from bs4 import BeautifulSoup

class Indeed():

    def __init__(self):

        self.domain = "https://pl.indeed.com"
        self.jobs = {}


    def get_data_from_website(self):

        i = 0
        while True:
            url = self.domain + "/jobs?q=&l=Pozna%C5%84%2C+wielkopolskie&radius=0&sort=date&fromage=3&start=" + str(i*10)
            class_check = "jobsearch-ResultsList"
            
            response = Scraper().open_url_selenium(url, class_check)
            if response:
                i += 1
                if not self.get_job_offers(response): break
            else:
                break


    def get_job_offers(self, html):

        bs = BeautifulSoup(html, 'html.parser')

        result_list = bs.find_all(attrs={"class": "jobsearch-ResultsList"})[0]
        list = result_list.find_all('li')

        new_job_counter = 0
        for li in list:
            
            a = li.find(attrs={"class": "jcs-JobTitle"})
            if a:
            
                href = self.domain + a['href']

                if not href in self.jobs:
                    new_job_counter +=1
                    self.jobs[href] = a.get_text()

        return new_job_counter            

    def show_data(self):

        for job in self.jobs:
            print(f"{job} :: {self.jobs[job]}")

