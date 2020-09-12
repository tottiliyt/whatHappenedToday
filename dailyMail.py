from bs4 import BeautifulSoup
import requests
import re

def get_links(news_website_link):
    res = requests.get(news_website_link)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    links_to_news_page = list()

    for link in soup.find_all('a'):
        if re.search('^htpps://www.dailymail.co.uk.*/article[0-9][0-9][0-9][0-9][0-9][0-9][0-9]', str(link.get('href'))):
            links_to_news_page.append(link.get('href'))
        if re.search('/article-[0-9][0-9][0-9][0-9][0-9][0-9][0-9]/', str(link.get('href'))):
            links_to_news_page.append('https://www.dailymail.co.uk' + link.get('href'))
        #print(link.get('href'))

    print(links_to_news_page)
    return links_to_news_page

get_links("https://www.dailymail.co.uk/ushome/index.html")