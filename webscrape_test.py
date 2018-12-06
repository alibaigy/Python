import urllib.request as ur
from bs4 import BeautifulSoup

url = "http://www.groupce.com/python/html/thejourney.html"
response = ur.urlopen(url)

html = response.read()

htmlsoup = BeautifulSoup(html, 'html.parser')

a_tags = htmlsoup('a')

for tag in a_tags:
    if 'Samara' in tag.contents[0]:
        print(tag)
        pagelink = tag.get('href')
       
if pagelink != '':
    
    url = pagelink
    
    response = ur.urlopen(url)
    html = response.read()
    htmlsoup = BeautifulSoup(html, 'html.parser')
    
    new_a_tags = htmlsoup('a')
    
    for tag in new_a_tags:
        print(tag) 