# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import time

#tworze klase wsbPLCheck dziedziczaca po klasie TestCase z modulu unittest
class WsbPLCheck(unittest.TestCase):

#instrukcje przed kazdym testem
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
#Metody rozpoczynajce sie od slowa 'test'
# czyli nasze testy
    def test_wsb_pl(self):
        driver=self.driver
        driver.get("http://www.wsb.pl")
        #sprawdzamy czy są na stronie " w tytule Wyższe szkoły bankowe"
        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)
        time.sleep(3)


#sprzatanie
def tearDown(self):
    pass


if __name__ == '__main__':
    unittest.main()
