#!/usr/bin/env python
# coding: utf-8

# In[54]:


from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')
tags = bs.find_all('ul')[3].find_all('li')
music_links = []
link_temp_list = []
for tag in tags:
    try:
        link_temp_list.append('http://en.wikipedia.org' + tag.a['href'])
    except:
        0 

music_links.extend(link_temp_list)
print(music_links)


# In[53]:


url=music_links[0]
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')
tags = bs.find_all('ul')[1].find_all('li')
music_links2 = []
link_temp_list = []
for tag in tags:
    try:
        link_temp_list.append('http://en.wikipedia.org' + tag.a['href'])
    except:
        0 

music_links2.extend(link_temp_list)
print(music_links2)


# In[52]:


name1=[]
yeras_active1=[]
for artist in music_links2:
    html = request.urlopen(artist)
    bs = BS(html.read(), 'html.parser')
    
    try:
        name = bs.find('h1').text
    except:
        name = ''
    name1.append(name)
    try:
        years_active = bs.find('th',string = 'Years active').next_sibling.text
    except:
        years_active = ''
    yeras_active1.append(years_active)
Dataframe=pd.DataFrame({'name':name1, 
                        'years active':yeras_active1})
print(Dataframe)

