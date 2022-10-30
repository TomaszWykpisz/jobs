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
        opt.headless = True # brak okienka
        opt.add_argument("--window-size=1920,1200")
        self.options = opt

    def openUrl(self, url, check_class):

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
