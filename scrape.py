from selenium import webdriver
import time

def search(text):
    searchBox = driver.find_element_by_id('gs_hdr_tsi')
    searchBox.send_keys(text)

    # wait for 5 sec and click the search button. 
    time.sleep(5)
    searchButton = driver.find_element_by_id('gs_hdr_tsb')
    searchButton.click()

    # Grab metadata of all pages
    meta_data = grab_metadata()
    print(meta_data)

def scrape_cited_papers(paper_name):
    pass

def grab_metadata():
    metadata = []
    list_of_elements = driver.find_elements_by_class_name('gs_ri')
    for e in list_of_elements:
        link = e.find_element_by_css_selector('a')
        author_pub = e.find_element_by_class_name('gs_a')
        citations = e.find_element_by_class_name('gs_fl').find_elements_by_css_selector('a')
        title = link.text
        author_pub_text = author_pub.text
        cited_by = citations[2].text
        metadata.append({
            'title': title,
            'author': author_pub_text,
            'citations': cited_by
        })
    return metadata

driver = webdriver.Firefox()

#URL of the website 
url = "https://www.scholar.google.com/"
   
#opening link in the browser
driver.get(url)
search("energy in software")

def constructQuery(keyword):
    pass



