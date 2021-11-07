# Build a web crawler that utilizes BFS

import requests
import re

class WebCrawler:

    def __init__(self):
        self.discovered = []

    def get_links_from_html(self, raw_html_url):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", raw_html_url)

    def read_html(self, url):
        raw_html = ''

        try:
            raw_html = requests.get(url).text

        except Exception:
            pass

        return raw_html

    def crawl(self, startUrl):

        queue = [startUrl]
        self.discovered.append(startUrl)

        while queue:
            actual_url = queue.pop(0)
            print(actual_url)

            actual_url_html = self.read_html(actual_url)

            for url in self.get_links_from_html(actual_url_html):
                if url not in self.discovered:
                    self.discovered.append(url)
                    queue.append(url)


if __name__ == '__main__':
    crawler = WebCrawler()

    crawler.crawl('https://www.cnn.com')