import pandas as pd
import requests
import time
from bs4 import BeautifulSoup


def crawl2df(titles, contents):
    return pd.DataFrame({'title': titles, 'contents': contents})


class Crawler:
    """
    page 번호에 접속, 하위 6개의 기사의 href와 타이틀을 가져옴
    """
    def __init__(self, main_url, main_css):
        self.__main_url = main_url
        self.__main_css = main_css
        self._href_list = []
        self._title_list = []

    def main_crawler(self):
        res = requests.get(self.__main_url)
        if res.status_code == 200:
            html = res.text
            soup = BeautifulSoup(html, 'html.parser')
            titles = soup.select(self.__main_css)

            for t in titles:
                self._title_list.append(t.text)
                self._href_list.append(t.attrs['href'])
        else:
            return res.status_code


class PHICrawler(Crawler):
    """
    main 페이지 내의 서브 기사들을 크롤링함.
    sub 기사들의 url_list는 부모 클래스에서 상속받음
    """
    sleep_time = 1

    def __init__(self, sub_css):
        super(PHICrawler, self).__init__()
        self.sub_css = sub_css
        self.__result_contents = []

    def phi_crawling(self):
        per_page_contents = []
        for s_url in self._href_list:
            res = requests.get(str(s_url))
            time.sleep(self.sleep_time)
            if res.status_code == 200:
                html = res.text
                soup = BeautifulSoup(html, 'html.parser')
                contents = []
                idx = 1
                while True:
                    try:
                        contents.append(soup.select(self.sub_css)[idx].text)
                        idx += 1
                    except IndexError:
                        idx = 1
                        break
            else:
                return res.status_code
            per_page_contents.append(' '.join(contents))
        self.__result_contents.extend(per_page_contents)

    def total_titles_contents(self):
        return list(set(self._title_list)), self.__result_contents
#
# c = Crawler("https://customs.gov.ph/category/news/page/1/", 'div > header > h2 > a')
# c.main_crawler()
# c.title_list
# c.href_list
#
#
# abc = '1'
# url = "https://customs.gov.ph/category/news/page/1/"
#
# res = requests.get(url)
# if res.status_code == 200:
#     html = res.text
#     soup = BeautifulSoup(html, 'html.parser')
#     titles = soup.select('div > header > h2 > a')
#
#
# for t in titles:
#     ttt = t.text
#     tt = t.attrs['href']
#     print(ttt, tt)
#
#
# url1 = "https://customs.gov.ph/boc-xip-continues-to-boost-its-scanning-performance-in-the-first-quarter-of-2022/"
# res = requests.get(url1)
#
# if res.status_code == 200:
#     html = res.text
#     soup = BeautifulSoup(html, 'html.parser')
#     title = soup.select('div.entry-content > p')[10]
#     # title = soup.findAll('p')
#     print(title.text)
#
# else:
#     print(response.status_code)
#
# #post-68744 > div > p:nth-child(3)
# #post-68744 > div > p:nth-child(4)
#
# aa = [1,2,3,4,5]
# bb = [2,3,4,5,6]
#
# pd.DataFrame({'title':aa, 'contents':bb})



