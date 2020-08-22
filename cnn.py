from bs4 import BeautifulSoup
import requests
import re


def get_links(news_website_link):
    res = requests.get(news_website_link)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    links_to_news_page = list()

    for link in soup.find_all('a'):
        print(link.get('href'))

    print(links_to_news_page)
    return links_to_news_page


def get_cnn_headline(links):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    web_text = []

    for web_links in get_links(links):
        res = requests.get(web_links, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        if soup.find('h1', attrs={'class': 'pg-headline'}) is not None:
            web_text.append(soup.find('h1', attrs={'class': 'pg-headline'}).text+' ')
    print(''.join(web_text))
    return ''.join(web_text)


def get_cnn_text(news_website_link):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    res = requests.get(news_website_link, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    headline_text = []
    for t in soup.find_all('span', {'class' : 'cd__headline-text'}):
        print(t.get_text())
        headline_text.append(t.get_text()+' ')

    return get_frequency(''.join(headline_text))

