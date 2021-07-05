from bs4 import BeautifulSoup
import requests
from pprint import pprint
from selenium import webdriver
import urllib
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import DriverManager as FirefoxDriverManager
from webdriver_manager.opera import DriverManager as OperaDriverManager
from selenium_stealth import stealth
import time
from bs4.builder import builder_registry

def main():
    global soup, next_link
    input_received = False
    first_create = False
    repo_links = []
    while(True):

        languages = []
        base_url = 'https://github.com'
        #url = 'https://github.com/cthacker-udel?tab=repositories'
        if not first_create:
            first_create = True
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
        else:
            print('{} <--- next link'.format(next_link))

        if not input_received:
            print('enter github username')
            url = 'https://github.com/' + input() + '?tab=repositories'
            br.get(url)
            time.sleep(2)
            orig_page_source = br.page_source
            input_received = True
            soup = BeautifulSoup(orig_page_source, "html.parser")
        else:
            br.get(next_link)
            time.sleep(2)
            next_page_source = br.page_source
            soup = BeautifulSoup(next_page_source,'html.parser')


        #soup = BeautifulSoup(orig_page_source,"html.parser")
        links = soup.find_all('a')
        spans = soup.find_all('span')
        #pprint(links)
        print('\n--------------\n')
        #pprint(spans)

        #acquiring linkf or next button

        #print(next_link)

        for eachlink in links:
            try:
                if eachlink['itemprop'] != None and 'codeRepository' in eachlink['itemprop']:
                    repo_links.append(eachlink['href'])
            except Exception as e:
                continue

        for eachrepolink in repo_links:
            br.get(base_url + eachrepolink)
            time.sleep(1)
            repo_page_source = br.page_source
            the_soup = BeautifulSoup(repo_page_source,'html.parser')
            the_soup_spans = the_soup.find_all('span')
            for eachspan in the_soup_spans:
                try:
                    eachspan_string = eachspan.string
                    if eachspan_string.lower() == 'python':
                        languages.append('Python')
                    elif eachspan_string.lower() == 'other':
                        languages.append('Other')
                    elif eachspan_string.lower() == 'java':
                        languages.append('Java')
                    elif eachspan_string.lower() == 'c':
                        languages.append('C')
                    elif eachspan_string.lower() == 'html':
                        languages.append('HTML')
                    elif eachspan_string.lower() == 'shell':
                        languages.append('Bash Shell')
                    elif eachspan_string.lower() == 'c++':
                        languages.append('C++')
                    elif eachspan_string.lower() == 'makefile':
                        languages.append('Makefile')
                    elif eachspan_string.lower() == 'css':
                        languages.append('CSS')
                except:
                    continue
        print(languages)

        next_found = False
        for eachlink in links:
            if eachlink.string != None and eachlink.string.lower() == 'next':
                try:
                    if eachlink['disabled']:
                        next_found = False
                        break
                except Exception as e:
                    next_link = eachlink['href']
                    next_found = True
                    break

        if not next_found:
            break

        br.get(next_link)






    #response = requests.get(url)

    #soup = BeautifulSoup(response.content,"html.parser")

    #pprint(soup)

    #tag1 = soup.find("ol",class_="d-flex").find_all("li",class_="mb-3")[0].child

    #pprint(tag1)

    #tag1 = soup.find_all("span",class_="repo")

    #repo_list = []

    #for eachtag in tag1:
    #    repo_list.append(eachtag.text.strip())

    #pprint(repo_list)




if __name__ == '__main__':
    main()