#__author: Liu Zheng
#date:2018/7/2

import requests
from bs4 import BeautifulSoup

url = 'http://desk.zol.com.cn/dongman/p4/'

def get_home_page():
    response = requests.get(url)
    return response.text

def parse_home_page(html):
    soup = BeautifulSoup(html,'lxml')
    print(soup.find_all(class_='pic'))
def main():
    html = get_home_page()
    get_home_page()
    parse_home_page(html)



if __name__=='__main__':
    main()