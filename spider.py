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

url = "http://bigbasket.com/cl/fruits-vegetables/?nc=nb"

def fileopen(chrome):
    print '1'
    page_source = chrome.page_source
    print '2'
    soup = BeautifulSoup(page_source,"html.parser")
    print '3'
    global split_folder
    print '4'
    folder = soup.find('div' , {'class':'uiv2-shopping-list-bredcom'})
    print '5'
    folder_text =folder.text
    print '6'
    split_folder = folder_text.split('>')
    print '7'
    files = soup.find('div' , {'id':'uiv2-title-breads-wrap'})
    print '8'
    files_name=files.find('h2').text
    print '9'
    global file
    print '10'
    try:
        print '11'
        if not os.path.exists(split_folder[0]+'/'+split_folder[1]):
            print '12'
            os.makedirs(split_folder[0]+'/'+split_folder[1])
            print '13'
    except Exception as ab:
        print '14'
        print(ab)
        print '15'
    file = open(split_folder[0]+'/'+split_folder[1]+'/'+files_name+'.txt',"a")
    print '16'
    return (file,split_folder)

def fileclose(file,wb):
    print '16'
    wb.save('products.xls')
    print '16'
    file.close()
    print '17'

def check(a,wb):
    print '18'
    if a==0:
        print '19'
        wb = copy(wb)
        print '20'  
    else:
        print '21'
        if a==1:
            print '22'
            sheet = wb.add_sheet('product-sheet')
            print '23'
            sheet.write(0,0,'ID')
            print '24'
            sheet.write(0,1,'Catogary')
            print '25'
            sheet.write(0,2,'Name')
            print '26'
            sheet.write(0,3,'Brand')
            print '27'
            sheet.write(0,4,'Price')
            print '28'
            sheet.write(0,5,'QTY')
            print '29'
            wb.save('products.xls')
            print '30'
    print '30'
    return wb
    
def load(chrome):
    i=1;
    print '31'
    try:
        print '32'
        wd = xlrd.open_workbook('products.xls')
        print '33'
        sheet = wd.sheet_by_name('product-sheet')
        print '34'
        rows = sheet.nrows
        print '35'
        i=rows
        print '36'
        a=0
        print '37'
    except:
        print '38'
        wb = xlwt.Workbook()
        print '39'
        a=1
        print '40'
    if a==1:
        print '41'
        check(a,wb)
        print '42'
    else:
        print '43'
        if a==0:
            print '44'
            check(a,wd)
            print '45'
    
    try:
        print '46'
        page_source = chrome.page_source
        print '47'
        global soup
        print '48'
        soup = BeautifulSoup(page_source,"html.parser")
        print '49'
        contents = soup.find_all('span' , {'class':'uiv2-tool-tip-hover '})
        print '50'
        qty = soup.find_all('span' , {'class':'dk_label'})
        print '51'
        rupee = soup.find_all('div' , {'uiv2-rate-count-avial'})
        print '52'
        fileopen(chrome)
        print '53'
        j=0
        print '54'
        i='1'
        print '55'
        try:
            print '551'
            try:
                wd = xlrd.open_workbook('products.xls')
            except Exception as exp:
                print exp
            print '552'
            wb = copy(wd)
            print '553'
            sheet = wb.get_sheet(0)
            print '56'
            for content in contents:
                splited = (content.text).split('-')
                splite= splited[0].split()
                print '57'
                sheet.write(i,0,i)
                print '58'
                sheet.write(i,1,split_folder[1])
                sheet.write(i,2,splited[0])
                sheet.write(i,3,splite[0])
                sheet.write(i,4,rupee[j].text)
                sheet.write(i,5,content.text)
                file.write(content.text+' '+rupee[j].text+'\n')
                j=j+1
                i=i+1
                print '59'
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
    print('No Button Found')
