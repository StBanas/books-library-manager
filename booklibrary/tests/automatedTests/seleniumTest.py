import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BookAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(50)
        # self.base_url = "http://srv08.mikr.us:30384/book/modify/add/mode/manual"
        self.base_url = "http://127.0.0.1:5000/book/modify/add/mode/manual"

    # def test_add_new(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     element = driver.find_element_by_name("author")
    #     try:
    #         element.clear()
    #     except:
    #         print("an exception occured")
    #     element.send_keys("Vladimir Nabokov")
    #     element = driver.find_element_by_name("title")
    #     try:
    #         element.clear()
    #     except:
    #         print("an exception occured")
    #     element.send_keys("Pale Fire")
    #     # element.submit()
    #     element.send_keys(Keys.RETURN)
    #     WebDriverWait(driver, 300).until(expected_conditions.title_contains("Library"))
    #     self.assertEqual(driver.title, "Library-Manual")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, warnings="ignore")