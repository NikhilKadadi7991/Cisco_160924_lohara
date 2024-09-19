from bs4 import BeautifulSoup 
import requests  
url = 'https://www.bbc.com/news'  
news_res = requests.get(url)  
soup = BeautifulSoup(news_res._content, 'html.parser')
headings = soup.find_all('h2')
with open('news_headings.txt', 'w',encoding='UTF-8') as new_file:
  for heading in headings:
    new_file.write(heading.text + '\n')     
print('BBC news Gathered')