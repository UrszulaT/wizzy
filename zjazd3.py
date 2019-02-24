# -*- coding: utf-8 -*-
#Zaimportowanie odpowiednich bibliotek
from selenium import webdriver
import time

#nowy ster do chrome
driver = webdriver.Chrome()
#maksymalizuje okno
driver.maximize_window()
#przejscie do strony web
driver.get("http://www.wsb.pl")
#wyswietl tytu strony
print (driver.title)
#popatrz przez 5 sekund
time.sleep(5)
#zamknij przegldarke
driver.quit()
