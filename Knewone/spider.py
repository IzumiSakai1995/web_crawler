#__author: Liu Zheng
#date:2018/7/2

import time
from bs4 import BeautifulSoup
import requests

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html,'lxml')
    imgs = soup.select('a.cover-inner.img')
    titles = soup.select('section.content.h4.a')
    links = soup.select('section.content.h4.a')
    for img,title,link in zip(imgs,titles,links):
        data = {
            'img':img.get('src'),
            'title':title.get('title'),
            'link':link.get('href'),
        }
        print(data)
        time.sleep(1)
def main():
    url = 'https://knewone.com/discover?page=1'
    html=get_page(url)
    parse_page(html)
if __name__ == '__main__':
    main()