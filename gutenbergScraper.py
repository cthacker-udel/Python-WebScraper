from bs4 import BeautifulSoup
import requests
import selenium
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib
from selenium import webdriver
from pprint import pprint

def main():

    try:
        br = webdriver.Firefox(FirefoxDriverManager().install())
    except Exception as e:
        try:
            br = webdriver.Chrome(ChromeDriverManager().install())
        except Exception as e:
            try:
                br = webdriver.Opera(OperaDriverManager().install())
            except Exception as e:
                print('Browser not found')
                return 0
    book_text = {}
    base_url_bookshelf = 'https://gutenberg.org/ebooks/bookshelf'
    base_url = 'https://gutenberg.org'
    br.get(base_url_bookshelf)
    while(True):
        print('')
        source_code = BeautifulSoup(br.page_source,'html.parser')
        all_links_src = source_code.find('div',class_="bookshelf_pages")
        all_links = all_links_src.find_all('a')
        book_links = []
        for eachlink in all_links:
            book_links.append(eachlink['href'])
        pprint(book_links)
        ### successfully gets all book links
        for eachbookshelf in book_links:
            br.get(base_url + eachbookshelf)
            soup = BeautifulSoup(br.page_source,'html.parser')
            all_book_spans = soup.find_all('span',class_='subtitle')
            pprint(all_book_spans)
            for eachspan in all_book_spans:
                br.get(base_url + eachspan.parent.parent['href'])
                book_soup = BeautifulSoup(br.page_source,'html.parser')
                book_name = book_soup.h1.string
                text_link = book_soup.find_all('a')
                for eachtextlink in text_link:
                    pprint('The link : {}'.format(eachtextlink))
                    try:
                        if eachtextlink['type'].lower() == 'text/plain; charset=utf-8':
                            ## found link for utf book
                            br.get(base_url + eachtextlink['href'])
                            book_text_soup = BeautifulSoup(br.page_source)
                            book_string = book_text.pre.string
                            license_index = book_string.find('*** END OF THIS PROJECT')
                            start_index = book_string.find('Gutenberg')
                            formatted_string = book_string[start_index+9:license_index]
                            book_text[book_name] = formatted_string.strip()
                            return 0
                    except Exception as e:
                        continue







if __name__ == '__main__':
    main()