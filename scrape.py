from selenium import webdriver
import time
import random 

def search(driver, text):
    """Search a text in scholar and get all results (10 pages max)"""
    searchBox = driver.find_element_by_id('gs_hdr_tsi')
    searchBox.send_keys(text)

    # wait for 5 sec and click the search button. 
    time.sleep(5)
    searchButton = driver.find_element_by_id('gs_hdr_tsb')
    searchButton.click()
    return __get_all_results(driver)

def scrape_by_url(driver, url, citations=None):
    driver.get(url)
    time.sleep(5)
    if(citations):
        page_count = int(citations/10) + 1
        return __get_all_results(driver, page_count)
    else:
        return __get_all_results(driver)

def __get_all_results(driver, page_count=None):
    if(not page_count):
        # Count the number of pages of results
        pages = driver.find_elements_by_css_selector('td')
        pages = pages[1:-1]
        page_count = len(pages)
        print(f"Number of pages of results = {len(pages)}")

    # Array to hold the results
    results = []

    # Grab the first page. 
    results += __grab_metadata(driver)

    # Grab metadata of all pages
    for page in range(2, page_count+1): #Skip first page since already done
        pagination = driver.find_element_by_css_selector('tr') # Refreshing the context
        try: 
            pagination.find_element_by_link_text(f"{page}").click()
        except:
            continue
        # page.find_element_by_css_selector('a').click() # click on the page number link
        time.sleep(random.randrange(5, 15)) # Delay of random seconds
        results += __grab_metadata(driver)
    return results


def __grab_metadata(driver): 
    """Grabs the content of the entire current page """
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


