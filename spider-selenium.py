from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
chrome.get('http://www.bigbasket.com/product/all-categories')
btn = chrome.find_element_by_id('uiv2-ftv-button')
btn.click()
print 'finding shit'
try:
    supercats = WebDriverWait(chrome, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class=dp_headding] a"), '')
        #chrome.find_elements_by_css_selector("div[class=dp_headding] a")
    )
finally:
    print 'shit found'
for cats in supercats:
    print cats.get_attribute('href')
    cats.click()
    container = chrome.find_element_by_id("products-container")

    products = container.find_elements_by_css_selector("li > .uiv2-list-box-img-title .uiv2-tool-tip-hover")
    for product in products:
        print product.text
    #load = chrome.find_element_by_id('more-products-load')

print 'bye'
chrome.close()
#driver.get("http://www.bigbasket.com")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("id_q")
#elem.send_keys("awesome")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()

