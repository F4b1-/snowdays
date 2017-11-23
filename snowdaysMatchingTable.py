import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class snowdaysMatchingTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost:3000/login")
        userNameField = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username")))
        userNameField.send_keys("admin")
        time.sleep(3)
        passwordField = driver.find_element_by_name("password")
        passwordField.send_keys("password")
        time.sleep(3)
        submitButton = driver.find_element_by_class_name("sn-btn-blue")
        submitButton.send_keys(Keys.RETURN)
        time.sleep(3)
        matchTab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "match")))
        matchTab.find_element_by_tag_name("a").click()
        time.sleep(3)
        matchingParticipantsTable = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "matchingParticipants")))
        matchingParticipantsTable.click()
        time.sleep(3)
	assert "MatchingParticipants_table" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
