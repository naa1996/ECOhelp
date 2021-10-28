import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test(self):

        s=Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
        browser.get('http://127.0.0.1:8000/reg')
        el_name = browser.find_element_by_name("username")
        el_name.send_keys("gffctftfffcfct")
        el_name = browser.find_element_by_name("username")
        el_name.send_keys("gffctftfffcfct")
        el_name = browser.find_element_by_name("username")
        el_name.send_keys("gffctftfffcfct")
        el_name = browser.find_element_by_name("username")
        el_name.send_keys("gffctftfffcfct")
        time.sleep(1000)

if __name__ == '__main__':
    unittest.main()
