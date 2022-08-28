from bs4 import BeautifulSoup
import requests 
from csv import writer

url = 'http://maps.hailstrike.com/category/hail-report/texas/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article')

with open('hail.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header= ['Location', 'data']
    thewriter.writerow(header)

    for list in lists:
        location = list.find('header', class_="entry-header").text.replace ('\n', '')
        data = list.find('span', class_="entry-tags").text.replace ('\n', '')
        info = [location, data]
        thewriter.writerow(info)
        