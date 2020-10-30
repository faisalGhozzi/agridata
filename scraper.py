import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=['Titre','Annee','Auteurs editeurs','Resume','lien'])

URL = 'https://onagri.home.blog/2020/08/19/veille-documentaire-de-lonagri/'

page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

results = soup.find(class_='post-content')

elements = results.find_all('p',class_='')

v=0

#removing the Strong tag
for e in elements:
    if ".pdf" in e.text.lower():
        v=1

if v == 1:
    print("we found a book")
else:
    print("lawej b3id")

'''strong_tag = soup.strong
strong_tag.decompose()

title = ''
year = ''
author = ''
resume = ''
link = ''

for i,e in  enumerate(elements):
    if i == 0:
        title = e.text
    elif i == 1:
        year = e.text[e.text.index(':')+2:]
    elif i == 2:
        author = e.text[e.text.index(':')+2:]
    elif i == 4:
        resume = e.text
    elif i == 5:
        link = e.find('a').contents[0]
df = df.append(pd.DataFrame([[title,year,author,resume,link]], columns=['Titre','Annee','Auteurs editeurs','Resume','lien']),ignore_index=True)

print(df.head())'''

#print('title  '+title+'\n')
#print('year  '+year+'\n')
#print('author  '+author+'\n')
#print('resume  '+resume+'\n')
#print('link   '+link)