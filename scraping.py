from bs4 import BeautifulSoup
import requests
import re
from flask import Flask
from flask import render_template
from flask import request
import nltk


app = Flask(__name__)


def get_links(news_website_link):
    res = requests.get(news_website_link)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    links_to_news_page = list()

    for link in soup.find_all('a'):
        if re.search('^http://news.yahoo.com/.*-[0-9][0-9][0-9][0-9]', link.get('href')):
            links_to_news_page.append(link.get('href'))
        if re.search('^/.*-[0-9][0-9][0-9][0-9]', link.get('href')):
            links_to_news_page.append('http://news.yahoo.com'+link.get('href'))

    print(links_to_news_page)
    return links_to_news_page


def get_title(links):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    web_text = []

    for web_links in links:
        res = requests.get(web_links, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        if soup.find('h1', attrs={'itemprop': 'headline'}) is not None:
            web_text.append(soup.find('h1', attrs={'itemprop': 'headline'}).text+' ')
    print(''.join(web_text))
    return ''.join(web_text)


def get_n(text):
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)
    nouns = [token[0] for token in tagged_tokens if token[1] in ['NN', 'NNS', 'NNP', 'NNPS']]
    frequency = nltk.FreqDist(nouns).most_common(100)
    print(frequency)
    return frequency


@app.route('/', methods=['POST', 'GET'])
def test_website():
    if request.method == "GET":
        print("GET")
        return render_template('test.html', message="GET")
    else:
        print("POST")
        source = request.form['input']
        frequency = get_n(get_title(get_links(source)))
    return render_template('test2.html', RESULT=str(frequency))


if __name__ == "__main__":
    app.run(debug=True)