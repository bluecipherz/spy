from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import any_text_present_in_element

url = "http://bigbasket.com/cl/fruits-vegetables/?nc=nb"
a=1
#url = 'http://bluecipherz.com'
#url = input('Enter URL:')

def scrollDown(chrome, numberOfScrollDown):
    body = chrome.find_element_by_tag_name('body')
    #chrome.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', eula)
    while numberOfScrollDown >=0:
        body.send_keys(Keys.PAGE_DOWN)
        numberOfScrollDown -= 1
        return chrome

def fileopen(chrome):
    page_source = chrome.page_source
    soup = BeautifulSoup(page_source,"html.parser")
    global split_folder
    folder = soup.find('div' , {'class':'uiv2-shopping-list-bredcom'})
    folder_text =folder.text
    split_folder = folder_text.split('>')
    files = soup.find('div' , {'id':'uiv2-title-breads-wrap'})
    files_name=files.find('h2').text
    global file
    global seed
    try:
        if not os.path.exists(split_folder[0]+'/'+split_folder[1]):
            os.makedirs(split_folder[0]+'/'+split_folder[1])
    except Exception as ab:
        print(ab)
    file = open(split_folder[0]+'/'+split_folder[1]+'/'+files_name+'.txt',"a")
    seed = open('seed.txt','a')
    return (file,seed,split_folder)

def fileclose(file,seed):
    file.close()
    seed.close()

def load(chrome):
    try:
        page_source = chrome.page_source
        global soup
        soup = BeautifulSoup(page_source,"html.parser")
        contents = soup.find_all('span' , {'class':'uiv2-tool-tip-hover '})
        qty = soup.find_all('span' , {'class':'dk_label'})
        rupee = soup.find_all('div' , {'uiv2-rate-count-avial'})
        fileopen(chrome)
        j=0
        i='1'
        try:
            for content in contents:
                splited = (content.text).split('-')
                splite= splited[0].split()
                #text = qtys.text
                #splited_text = text.split('(',1)[0]
                #qty_price=splited_text.split('-')
                seed.write("'id' => ' "+i+ "', "+ "'path' => ' "+split_folder[0]+ "', "+ "'main-cat' => ' "+split_folder[1]+ "', "+ "'brand' => ' "+splite[0]+ "', "+ "'name' => ' "+splited[0]+ "', "+ "'price' => ' "+rupee[j].text+ "', "+ "'qty' => ' "+content.text+ ", \n")
                file.write(content.text+' '+rupee[j].text+'\n')
                j=j+1
            fileclose(file,seed)
            print('ok Done')
        except Exception as ae:
            print(ae)
    except:
        print('something went wrong')

def check(path):
    try:
        el2 = el1.find_element_by_id(path)
        return el2
    except NoSuchElementException:
        el2.text='not there'
        return el2.text

#--------------------------Code--Start-----------------------------------

global chrome
chrome = webdriver.Chrome()
chrome.get(url)
try:
    btn = chrome.find_element_by_id('uiv2-ftv-button')
    print('going to click the button')
    btn.click()
except:
    print('No Button Fount')
#-------------------------------------------------------------------------
try:        
    print('waiting')
    WebDriverWait(chrome, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[id=products-container]"), ''))
    container = chrome.find_element_by_id("products-container")
    el1 = container.find_element_by_class_name('jscroll-inner')
    el2 = check('next-product-page')
    #---------------------------------------------------------------------
    while check('next-product-page').text != 'Show More Pages':
        chrome = scrollDown(chrome,20)
        #e13 = 
        #chrome.execute_script("return arguments[0].scrollIntoView();", el3)
        time.sleep(0.5)
        container = chrome.find_element_by_id("products-container")
        el1 = container.find_element_by_class_name('jscroll-inner')
        time.sleep(0.5)
        el2 = check('next-product-page')
        if(el2.text =='Show More Pages'):
            break
    #---------------------------------------------------------------------
    container = chrome.find_element_by_id("products-container")
    el1 = container.find_element_by_class_name('jscroll-inner')
    time.sleep(0.5)
    el2 = check('next-product-page')
    #---------------------------------------------------------------------
    while el2.text == 'Show More Pages':
        el2.click()
        chrome.execute_script("return arguments[0].scrollIntoView();", el2)
        time.sleep(0.5)
        container = chrome.find_element_by_id("products-container")
        el1 = container.find_element_by_class_name('jscroll-inner')
        time.sleep(2)
        el2 = check('next-product-page')
        if(el2.text !='Show More Pages'):
            break

    load(chrome)
    
except :
    print('nop')
    load(chrome)
#-------------------------------------------------------------------------
