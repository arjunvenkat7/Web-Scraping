# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 06:01:24 2018

@author: Arjun
"""

#Web scraping from news webistes wire.in and firstpost.com
#I am using BeutifulSoup since its easier to understand and implement
from bs4 import BeautifulSoup as bs
#from lxml import html
import requests
page = requests.get('https://thewire.in/')
soup = bs(page.content, 'html.parser')
f = open('news_data.txt','w')
#in Wire's website, each news article is inside a class called card title
#For now I have just focussed on getting the headlines alone
mydiv = soup.find_all('div', {'class':'card__title'})
#print(len(mydiv))
#All the news articles are in the format of anchor tags, So title is segregated
#to get the news content
for m in mydiv:
    each = m.find('a')
    title = each.get('title')
    f.write('\n'+title)
    #print(title)
    
#Getting news articles from firstpost    
page1 =requests.get('https://www.firstpost.com/')
soup1 = bs(page1.content, 'html.parser')
#In firstpost, the headlines are present under trending section class
mydiv1 = soup1.find_all('section',{'class':'trending section'})    
print(len(mydiv1))
#Since the news headlines are written different header tags,I capture all the neccessary ones
each = soup1.find_all(['h2','h3','h4'])
#print(each)
for e in each:
    text  = e.get_text()
    f.write('\n'+text)
    #print(text)
f.close()
#For file operation I use overwrite, So everytime I run the code the older news are deleted
#I get the latest news from the websites