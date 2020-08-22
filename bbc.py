from bs4 import BeautifulSoup
import requests
import re


def get_links(news_website_link):
    res = requests.get(news_website_link)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    links_to_news_page = list()

    for link in soup.find_all('a'):
        if re.search('^https://www.bbc.com/.*[0-9][0-9][0-9][0-9][0-9][0-9]', link.get('href')):
            links_to_news_page.append(link.get('href'))
        elif re.search('^https://www.bbc.co.uk/.*[0-9][0-9][0-9][0-9][0-9][0-9]', link.get('href')):
            links_to_news_page.append(link.get('href'))
        elif re.search('[0-9][0-9][0-9][0-9][0-9][0-9]', link.get('href')):
            links_to_news_page.append('https://www.bbc.com' + link.get('href'))

    print(links_to_news_page)
    return links_to_news_page


get_links("https://www.bbc.com/news")