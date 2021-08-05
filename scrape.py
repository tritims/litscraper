from selenium import webdriver

def search(text):
    searchBox = driver.find_element_by_id('gs_hdr_tsi')
    searchBox.send_keys(text)

    # wait for 5 sec and click the search button. 


driver = webdriver.Firefox()

#URL of the website 
url = "https://www.scholar.google.com/"
   
#opening link in the browser
driver.get(url)
search("ff")

def constructQuery(keyword):
    pass

