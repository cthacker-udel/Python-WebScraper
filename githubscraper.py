from bs4 import BeautifulSoup
import requests
from pprint import pprint

def main():

    print('enter github username')
    url = 'https://github.com/' + input()

    response = requests.get(url)

    soup = BeautifulSoup(response.content,"html.parser")

    tag1 = soup.find_all("span",class_="repo")

    repo_list = []

    for eachtag in tag1:
        repo_list.append(eachtag.text.strip())

    pprint(repo_list)




if __name__ == '__main__':
    main()