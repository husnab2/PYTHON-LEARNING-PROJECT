from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import json
import os
import unittest

class SearchPage(BasePage):

  def __init__(self, driver, testData):
    super().__init__(driver)
    self.driver = driver
    print(f'test file %s',testData)
    script_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', testData))
    print(script_dir)
    self.testData = json.load(open(script_dir))

  def navigate_jobsearch_url(self):
    self.driver.get("https://jobserve.com/gb/en/Job-Search/")

  def populate_form(self):
    self.driver.find_element(By.ID, "txtKey").send_keys(self.testData["keyWords"])
    self.driver.find_element(By.ID, "txtLoc").send_keys(self.testData["location"])
    self.driver.find_element(By.ID, "selRad").send_keys(self.testData["locationMiles"])
    self.driver.find_element(By.ID, "selAge").send_keys(self.testData["posted"])
    self.driver.find_element(By.ID, "selJType").send_keys(self.testData["jobType"])
    self.driver.find_element(By.ID, "btnSearch").click()

  def verify_search_result(self):
    jobResult = self.testData["jobResult"]
    actualJobResult = self.driver.find_element(By.CSS_SELECTOR, ".jobshead").text
    print(actualJobResult)
    unittest.TestCase.assertTrue(self,jobResult["jobsHeadingText"] in actualJobResult, "success")
