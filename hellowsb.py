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

#sprzatanie
    def tearDown(self):
        self.driver.quit()

#Metody rozpoczynajce sie od slowa 'test'
# czyli nasze testy
    def test_wsb_pl(self):
        driver=self.driver
        driver.get("https://www.wsb.pl")
        #sprawdzamy czy są na stronie " w tytule Wyższe szkoły bankowe"
        self.assertIn("Wyższe Szkoły Bankowe".decode("utf-8"), driver.title)
        time.sleep(3)


    # def test_link(self):
    #     driver = self.driver
    #     driver.get("https://wwww.wsb.pl")
    #     driver.find_element_by_link_text("Studia II stopnia").click()
    #     time.sleep(5)


    # def test_select(self):
    #     driver =  self.driver
    #     driver.get("http://www.wsb.pl")
    #     driver.find_element_by_id("edit-city")
    #     time.sleep(5)
    #
    # def test_select(self):
    #     driver = self.driver
    #     driver.get("https://www.wsb.pl")
    #     select-city = select(driver.find_element_by_name)


if __name__ == '__main__':
    unittest.main()
