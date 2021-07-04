import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

def main():
    url = 'https://realpython.github.io/fake-jobs/'
    page = requests.get(url)

    #pprint(page.text)

    soup = BeautifulSoup(page.content,"html.parser")

    job_listings = soup.find(id="ResultsContainer")

    #pprint(job_listings)

    all_jobs = job_listings.find_all("div",class_="card-content")

    for job_element in all_jobs:
        print('--------------\n')
        pprint(job_element)
        media_right = job_element.find("div",class_="media-content")
        title_content = media_right.find("h2",class_="title")
        subtitle_content = media_right.find("h3",class_="subtitle")
        content_ = job_element.find("div",class_="content")
        location_ = content_.find("p",class_="location")
        job_posting_date_class = content_.find("p",class_="is-small")
        pprint(content_.time.text.strip())
        #pprint(title_content)
        #pprint(subtitle_content)
        print(subtitle_content.text.strip())
        print(location_.text.strip())
        print(title_content.text.strip())





if __name__ == '__main__':
    main()