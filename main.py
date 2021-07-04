import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

def main():
    url = 'https://realpython.github.io/fake-jobs/'
    page = requests.get(url)

    pprint(page.text)



if __name__ == '__main__':
    main()