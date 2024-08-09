import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDBSearchPage:

   def __init__(self, driver):
       self.driver = driver
       self.expandall = (By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button')
       self.name_input = (By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input")
       self.awards = (By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[5]/div[2]/div/div/section/button[1]")
       self.search_within_topic = (By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[5]/div[2]/div/div/div[2]/div/div/div/select")
       self.search_button = (By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button')

   def open(self):
       self.driver.get("https://www.imdb.com/search/name/")
       self.driver.maximize_window()

   def scroll_down(self):
       self.driver.execute_script("window.scrollTo(1200, 1200);")

   def fill_search_form(self, name, searchby):
       # expand all
       self.driver.find_element(by=By.XPATH, value=self.expandall).click()
       # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.expandall)).click()
       # # name input
       self.driver.find_element(by=By.XPATH, value=self.name_input).send_keys(name)
       # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_input)).send_keys(name)
       time.sleep(3)
       self.scroll_down()
       # awards recognition
       self.driver.find_element(by=By.XPATH, value=self.awards[1]).click()
       # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.awards)).click()
       time.sleep(3)

       # Drop Down
       element = self.driver.find_element(by=By.XPATH, value=self.search_within_topic[1])
       select = Select(element).select_by_value(searchby)
       time.sleep(3)

   def click_search(self):
       WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_button)).click()
       time.sleep(10)
