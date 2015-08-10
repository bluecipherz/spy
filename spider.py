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

def fileclose(file):
    file.close()

def check(a)
    if a==0:
        wb = copy(wd)
    else if a==1:
        sheet = wb.add_sheet('product-sheet')
        sheet.write(0,0,'Catogary')
        sheet.write(1,0,'Name')
        sheet.write(2,0.'Brand')
        sheet.write(3,0,'Price')
        sheet.write(4,0,'QTY')
        wb.save('products.xls')
    return wb
    
def load(chrome):
    try:
        wd = xlrd.open_workbook('products,xls')
        sheet = wd.sheet_by_name('product-sheet')
        rows = sheet.nrows -1
        a=0
    except:
        wb = xlwt.Workbook()
        a=1
    check(a)
    
