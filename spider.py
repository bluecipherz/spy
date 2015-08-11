from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import xlwt
import xlrd
from xlutils.copy import copy

url = "http://bigbasker.com/cl/fruits-vegetables/?nc=nb"

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
    return (file,split_folder)

def fileclose(file,wb):
    wb.save('products.xls')
    file.close()

def check(a):
    if a==0:
        wb = copy(wd)
    else:
        if a==1:
            sheet = wb.add_sheet('product-sheet')
            sheet.write(0,0,'ID')
            sheet.write(0,1,'Catogary')
            sheet.write(0,2,'Name')
            sheet.write(0,3,'Brand')
            sheet.write(0,4,'Price')
            sheet.write(0,5,'QTY')
            wb.save('products.xls')
    return wb
    
def load(chrome):
    i=0;
    try:
        wd = xlrd.open_workbook('products.xls')
        sheet = wd.sheet_by_name('product-sheet')
        rows = sheet.nrows
        i=rows
        a=0
    except:
        wb = xlwt.Workbook()
        a=1
    check(a)
    
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
                sheet.write(i,0,i)
                sheet.write(i,1,split_folder[1])
                sheet.write(i,2,splited[0])
                sheet.write(i,3,splite[0])
                sheet.write(i,4,rupee[j].text)
                sheet.write(i,5,content.text)
                file.write(content.text+' '+rupee[j].text+'\n')
                j=j+1
                i=i+1
            fileclose(file,wb)
            print('ok Done')
        except Exception as ae:
            print(ae)
    except:
        print('something went wrong')

global chrome
chrome = webdriver.Chrome()
chrome.get(url)
try:
    btn = chrome.find_element_by_id('uiv2-ftv-button')
    print('going to click the button')
    btn.click()
except:
    print('No Button Fount')
