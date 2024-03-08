import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions

driver = webdriver.Chrome()
driver.get("https://www.ravelry.com/stash/search#colorway-link=200-nymphwood&photo=yes&view=thumbs&yarn-link=lion-brand-mandala")
results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)