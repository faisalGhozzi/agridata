import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

df = pd.read_csv('article_links.csv',index_col='id')

def fetch_infos(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find(class_='post-content')
    result_h1 = soup.find(class_='post-title')
    elements = results.find_all('p')

    v = False
    for e in elements:
        if len(e.text) < 1:
            elements.remove(e)

    if len(elements) > 0:
        if len(elements[-1].text) == 0:
            if '.pdf' in elements[-2].text.lower():
                link = elements[-2].find('a')['href']
        elif '.pdf' in elements[-1].text.lower():
            link = elements[-1].find('a')['href']
        else:
            link = ''
    
        if len(link) == 0:
            return None
        else:
            return [result_h1.text,link]
    
def return_column_as_list(data):
    return data['link'].tolist()

def browse_links_lists_and_add_to_dataFrame(data):
    links_list = return_column_as_list(data)
    books_elem = []
    for link in links_list:
        if fetch_infos(link) != None:
            books_elem.append(fetch_infos(link))
    return books_elem

def run():
    books_list = browse_links_lists_and_add_to_dataFrame(df)
    new_df = pd.DataFrame()

    extracted_book = []
    extracted_book_list = []

    for b in books_list:
        new_df = new_df.append(pd.DataFrame(data=[b],columns=["livre","lien"]))
    new_df.index = [x for x in range(1,len(new_df.values)+1)]
    new_df.to_csv('books.csv')

run()
#fetch_infos('https://onagri.home.blog/2020/06/22/carbone-organique-du-sol-une-richesse-invisible/')
