import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import pandas as pd

df = pd.DataFrame(columns=['link'])

base_URL = 'https://onagri.home.blog/'

driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\Integration\\Pidev Desktop\\Jars\\chromedriver.exe")

driver.get(base_URL)

page = driver.execute_script('return document.body.innerHTML')

soup = BeautifulSoup(''.join(page),'html.parser')

results = soup.find(id='posts')

posts = results.find_all('article')

list = []

for post in posts:
    df = df.append(pd.DataFrame([[post.find('a')['href']]],columns=['link']),ignore_index=True)

#df.to_csv('article_links.csv')