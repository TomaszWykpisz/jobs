import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Scraper():

    def __init__(self):

        self.service = Service('C:\\Users\\Tomek\\Desktop\\python\\chromedriver.exe')
        
        opt = Options()
        #opt.headless = True 
        opt.add_argument("--window-size=1920,1200")
        self.options = opt

    def open_url_selenium(self, url, check_class):

        driver = webdriver.Chrome(options=self.options, service=self.service)
        driver.get(url)
        ret = ''
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(('class name', check_class)))
        except TimeoutException:
            print(f'Cannot open:\n', url)
        else:
            ret = driver.page_source
            print(f'Ok open:\n',url)
        finally:
            driver.quit()
            return ret

    def open_url_request(self, url):
        ret = ''
        try:
            r = requests.get(url)
            ret = r.text
            print(f'Ok open:\n',url)
        except: 
            print(f'Cannot open:\n', url)
            pass
        return ret