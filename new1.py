from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
import xlwt
import xlrd
from xlwt import easyxf
from xlrd import open_workbook
from xlutils.copy import copy

url='www.bigbasket.com'
def load(chrome):
    i=1;
    try:
        wb = xlrd.open_workbook('products.xls',formatting_info=True)
        sheet = wb.sheet_by_index(0)
        i = sheet.nrows
        print 'i=',i
        sheet=''
        a=0
    except Exception as exp:
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('bigbasket')
        a=1

    if a==0:
        wb = copy(wb)
        sheet = wb.get_sheet(0)
    if a==1:
        sheet.write(0,0,'ID')
        sheet.write(0,1,'Catogary')
        sheet.write(0,2,'Brand')
        sheet.write(0,3,'Name')
        sheet.write(0,4,'QTY')
        sheet.write(0,5,'Price')
    try:
        page_source = chrome.page_source
        soup = BeautifulSoup(page_source,"html.parser")
        contents = soup.find_all('span' , {'class':'uiv2-tool-tip-hover '})
        qty = soup.find_all('span' , {'class':'dk_label'})
        rupee = soup.find_all('div' , {'uiv2-rate-count-avial'})
        folder = soup.find('div' , {'class':'uiv2-shopping-list-bredcom'})
        folder_text =folder.text
        split_folder = folder_text.split('>')
        files = soup.find('div' , {'id':'uiv2-title-breads-wrap'})
        files_name=files.find('h2').text
        try:
            if not os.path.exists(split_folder[0]+'/'+split_folder[1]):
                os.makedirs(split_folder[0]+'/'+split_folder[1])
        except Exception as ab:
            print(ab)
        file = open(split_folder[0]+'/'+split_folder[1]+'/'+files_name+'.txt',"a")
        j=0
        wb.save('products.xls')
        for content in contents:
            splited = (content.text).split('-')
            splite= splited[0].split()
            sheet.write(i,0,i)
            sheet.write(i,1,split_folder[1])
            sheet.write(i,2,splite[0])
            sheet.write(i,3,splited[0])
            sheet.write(i,4,content.text)
            sheet.write(i,5,rupee[j].text)
            file.write(content.text+' '+rupee[j].text+'\n')
            i=i+1
            j=j+1
        print 'exited for loop'
        wb.save('products.xls')
    except Exception as ae:
        print(ae)
try:
    chrome = webdriver.Chrome()
    chrome.get(url)
except Exception as exp:
    print exp
