from pproject.keyword_extraction.crawling import crawl2df, Crawler, PHICrawler
from tqdm import tqdm
import time


def crawl_phi_boc():
    titles, contents = [], []
    for idx in tqdm(range(1, 337)):
        c = Crawler(main_url="https://customs.gov.ph/category/news/page/{}/".format(idx),
                    main_css="div > header > h2 > a")
        pc = PHICrawler(sub_css="div.entry-content > p")
        c.main_crawler()
        time.sleep(0.1)
        pc.phi_crawling()
        t_list, c_list = pc.total_titles_contents()
        titles.extend(t_list)
        contents.extend(c_list)
    result = crawl2df(titles=titles, contents=contents)

    return result


if __name__ == '__main__':
    result = crawl_phi_boc()
    result.to_csv('phi_crawling_data.csv')
