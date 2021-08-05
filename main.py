import scrape as sp
from selenium import webdriver

driver = webdriver.Firefox()

# url = "https://scholar.google.com/scholar?cites=1540023752404201374&as_sdt=2005&sciodt=0,5&hl=en"
url = "https://scholar.google.com/scholar?cites=5536417177425935557&as_sdt=2005&sciodt=0,5&hl=en"

sp.scrape_by_url(driver, url=url, citations=148)



