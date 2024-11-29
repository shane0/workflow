#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pdb


SITE = "https://shanenull.com/buddhism/2024/"
TITLE_TEXT = "shane0 buddhism"
try:
    driver = webdriver.Firefox()
    driver.get(SITE)
    assert TITLE_TEXT in driver.title
    print("Assertion passed: Title contains 'shane0 buddhism'")
except AssertionError:
    print("Assertion failed: Title does not contain 'shane0 buddhism'")
# <input type="text" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="none" autocorrect="off" autocomplete="off" spellcheck="false" data-md-component="search-query" required="">
try:
    element_name = "query"
    elem = driver.find_element(By.NAME, element_name)
    elem.send_keys("maranasati")
    elem.send_keys(Keys.RETURN)
    assert "maranasati" in driver.page_source
    print("search passed")
except AssertionError:
    print("An exception occurred finding search element")
# time.sleep(60)
# pdb.set_trace()
driver.close()
