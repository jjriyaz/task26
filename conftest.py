from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages import IMDBSearchPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
  chrome_options = Options()
  chrome_options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(options=chrome_options)
  yield driver
  # driver.quit