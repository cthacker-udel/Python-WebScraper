from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import  DriverManager as FirefoxDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.manager import DriverManager
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import time
from pprint import pprint


def main():

    ## initializing driver

    base_url = 'https://imsdb.com'

    try:
        br = webdriver.Chrome(ChromeDriverManager().install())
    except Exception as e:
        try:
            br = webdriver.Firefox(FirefoxDriverManager().install())
        except Exception as e:
            try:
                br = webdriver.Opera(OperaDriverManager().install())
            except Exception as e:
                try:
                    br = webdriver.Edge(EdgeChromiumDriverManager().install())
                except Exception as e:
                    try:
                        br = webdriver.Safari(DriverManager.install())
                    except Exception as e:
                        print('No available browser detected, please import chrome, firefox, opera, edge, or safari to utilize program')
                        return 0
    br.get(base_url)
    first_soup = BeautifulSoup(br.page_source,'html.parser')
    all_first_soup_links = first_soup.find_all('a')
    genre_links = []
    for eachlink in all_first_soup_links:
        try:
            #pprint(eachlink.attrs)
            if 'genre' in eachlink['href']:
                genre_links.append(eachlink['href'])
        except Exception as e:
            continue
    ## goto genre
    script_page_locations = []
    for eachlink in genre_links:
        br.get(base_url + eachlink)
        page_soup = BeautifulSoup(br.page_source,'html.parser')
        all_links = page_soup.find_all('p')
        for eachp in all_links:
            script_page_locations.append(eachp.contents[0]['href'])
        #time.sleep(5)
    script_text_links = []
    for eachlink in script_page_locations:
        br.get(base_url + eachlink)
        all_page_links = BeautifulSoup(br.page_source,'html.parser').find_all('a')
        for eachlink in all_page_links:
            if eachlink.string != None and 'Read' in eachlink.string:
                script_text_links.append(eachlink['href'])
    all_movie_text = []
    for eachscripttextlink in script_text_links:
        br.get(base_url + eachscripttextlink)
        script_soup = BeautifulSoup(br.page_source)
        all_movie_text.append(script_soup.find('pre').string)
    pprint("Text = {}".format(all_movie_text))






if __name__ == '__main__':
    main()





