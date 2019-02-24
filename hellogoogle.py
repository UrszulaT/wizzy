# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
import time

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
        pass

    def test_search(self):
        driver = self.driver
        driver.get("http://www.google.pl")
        input = driver.find_element_by_name("q")
        input.send_keys("Chorzów")
        time.sleep(3)
        pass

if __name__ == '__main__':
    unittest.main()
