import unittest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tauk.tauk_webdriver import Tauk
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv(".env")
Tauk()


class TaukTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        Tauk.register_driver(self.driver, unittestcase=self)
        self.driver.get("https://www.tauk.com/welcome")

    def tearDown(self):
        self.driver.quit()