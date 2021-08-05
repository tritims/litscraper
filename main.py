import scrape as sp
from selenium import webdriver
import pandas as pd
driver = webdriver.Firefox()

# url = "https://scholar.google.com/scholar?cites=1540023752404201374&as_sdt=2005&sciodt=0,5&hl=en"
url = "https://scholar.google.com/scholar?cites=5536417177425935557&as_sdt=2005&sciodt=0,5&hl=en"

# Give url and the number of citations as input
data = sp.scrape_by_url(driver, url=url, citations=184)
pd.DataFrame(data).to_csv('results.csv')



