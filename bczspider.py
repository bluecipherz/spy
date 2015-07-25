from BeautifulSoup import BeautifulSoup
from mechanize import Browser
br = Browser()
rsp = br.open('http://bigbasket.com')
page = rsp.read()
soup = BeautifulSoup(page)
basket = soup.find("nav", {"id":"basket_menu"})
items = basket.findAll("li")
for items in items:
	print items.
