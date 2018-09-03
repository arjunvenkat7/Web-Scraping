# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 07:38:38 2018

@author: Arjun
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
url = '########' #Masking the URL since I am not sure if I can use the source website directly
# Am using the selenium part to click on translate button for english language
# The website initially loads in Finnish
driver = webdriver.Chrome('Location of your chrome driver')
driver.implicitly_wait(30)
driver.get(url)
python_button = driver.find_element_by_id('ImgBtFin') 
python_button.click()
soup = bs(driver.page_source, 'html.parser')#Parsing the HTML page
file = open('Location to open your notepad/file and write the contents')
mydiv = soup.find_all('div', {'class':'col-xs-12 first-title'})# All the information about menu are present inside div tag
#Once all the elements are parsed we can segregate the menu items alone
for m in mydiv:
    title = m.get_text()
    print(type(title))
    file.write('\n'+title)
file.close()
#If you want to rewrite contents everytime the code is run, close the file and open it in w mode when writing contents
with open("FIle location") as f:
    lines = f.read().splitlines()
#reading the contents from the file
lines = list(filter(None, lines))#remove all the blank empty lines
n_list = [x for x in lines if x != 'Täytteet:  ']#temp variable to hold all lines except for the ones word topping, since it repeats in all menu items
toppings  = n_list[1::2]#Sgregating the toppings alone ignoring pizza name 
t_list = [y for x in toppings for y in x.split(',')]#Segreagting each topping as a separate string 
t_list = set(t_list)#removing duplicates
#Creating a dictionary so that we can easily keep track of each topping and its occurences
toppings_count = {}
for t in t_list:
    toppings_count[t] = t_list.count(t)

#Sorting the dictionary in descending order
sorted_toppings = [(k, toppings_count[k]) for k in sorted(toppings_count, 
                   key=toppings_count.get, reverse=True)]
#Not required to do but am doing it for getting into conclusion quickly
#Plotting the toppings and its occurences
fig, ax = plt.subplots()
plt.figure()
ax.bar(range(len(sorted_toppings)), [t[1] for t in sorted_toppings]  , align="center")
ax.set_xticks(range(len(sorted_toppings)))
ax.set_xticklabels([t[0] for t in sorted_toppings])
fig.autofmt_xdate()#Using it to avoid congestion in xticks
plt.show()
#Alternatively we can split the toppings and genearte two subplot for readability    
        