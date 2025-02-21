from selenium import webdriver
import os

def create_driver():
  value = os.environ.get('browser')
  featuresPath = os.environ.get('FEATURES_PATH')
  print(featuresPath)
  behavexPath = os.environ.get('BEHAVEX_PATH')
  print(behavexPath)
  if value == 'chrome':
    print(value)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=10)
    return driver
  elif value == 'firefox':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(time_to_wait=10)
    return driver