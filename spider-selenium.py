from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
chrome.get('http://www.bigbasket.com/product/all-categories')
btn = chrome.find_element_by_id('uiv2-ftv-button')
btn.click()
print 'waiting'
try:
    WebDriverWait(chrome, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class=dp_headding] a"), '')
    )
finally:
    print 'wait finished'
    supercats = chrome.find_elements_by_css_selector("div[class=dp_headding] a")
    for cats in supercats:
        print cats.get_attribute('href')

        #cats.click()
        #container = chrome.find_element_by_id("products-container")

        #products = container.find_elements_by_css_selector("li > .uiv2-list-box-img-title .uiv2-tool-tip-hover")
        #for product in products:
            #print product.text
        #load = chrome.find_element_by_id('more-products-load')
for cats in supercats:
    cats.click()
    try:        
        WebDriverWait(chrome, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[id=more-products-load]"), '')
        )
    finally:
    #chrome.get(cats.get_attribute('href'))
        container = chrome.find_element_by_id("products-container")

        products = container.find_elements_by_css_selector("li > .uiv2-list-box-img-title .uiv2-tool-tip-hover")
        for product in products:
            print product.text

print 'bye'
#chrome.close()
