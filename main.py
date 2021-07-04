import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import regex as re

def main():
    url = 'https://realpython.github.io/fake-jobs/'
    page = requests.get(url)

    #pprint(page.text)

    soup = BeautifulSoup(page.content,"html.parser")

    job_listings = soup.find(id="ResultsContainer")

    #pprint(job_listings)

    python_jobs = job_listings.find_all("h2",string=lambda text: 'python' in text.lower())

    count = 1
    for eachjob in python_jobs:
        #pprint(eachjob.parent.parent.parent.parent)
        role = eachjob.parent.find("h2",class_="title").text.strip()
        company_name = eachjob.parent.find("h3",class_="subtitle").text.strip()
        logo_link = eachjob.parent.parent.img['src'].strip()
        time_of_posting = eachjob.parent.parent.parent.time.text.strip()
        location = eachjob.parent.parent.parent.parent.find("p",class_="location").text.strip()
        link_to_apply = eachjob.parent.parent.parent.parent.find("a",string=re.compile("[aA]pply"))['href'].strip()
        print('\n----- Job {} -----\nRole : {}\nName : {}\nLogo Link : {}\nTime of Posting : {}\nLocation : {}\nLink To Apply : {}\n----------------------'.format(count,role,company_name,logo_link,time_of_posting,location,link_to_apply))
        count += 1

    #first_tag = python_jobs[0]

    #pprint(first_tag.parent.parent.parent)

    #all_jobs = job_listings.find_all("div",class_="card-content")
    """
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
    """





if __name__ == '__main__':
    main()