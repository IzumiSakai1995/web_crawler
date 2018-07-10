#__author: Liu Zheng
#date:2018/7/7

import re
import requests
#from bs4 import BeautifulSoup


def get_one_page(url):
    response = requests.get(url)
    return response.text

def parse_one_page(html):
    # soup = BeautifulSoup(html,'lxml')
    # result = soup.select('div[class="content"] > span')
    # return result

    pattern = re.compile('<div class="author clearfix">.*?atl="(.*?)"></div>')
    result = re.findall(pattern,html)
    return result
def main():
    url = 'https://www.qiushibaike.com/'
    html = get_one_page(url)
    print(parse_one_page(html))

if __name__ == '__main__':
    main()