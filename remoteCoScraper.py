from bs4 import BeautifulSoup
import requests
from pprint import pprint

def main():

    url = 'https://remote.co'

    remote_co_html = requests.get(url)

    soup = BeautifulSoup(remote_co_html.content,"html.parser")

    #the_main_class = soup.find("body",class_="home blog remote-co").main.find("div",class_="container pt-4").find("div",class_="row").find("div",class_="col").find_all("div",class_="card bg-light mb-3").find("div")

    the_main_class = soup.main.find("div",class_="container pt-4").find_all("div",class_="card bg-light mb-3")[1].find("div",class_="card-body").find_all("div",class_="card-deck")#

    for eachmarker in the_main_class:
        each_card = eachmarker.find_all('div',class_='card')
        for each_job in each_card:
            print(each_job.img['alt'])
        #for each_entry in each_card:
        #    each_job = each_entry.find('div',class_='card-body').img['alt']
        #    print(each_job)
        #pprint(the_job)
    #[0].find('div',class_='card-body').img['alt']

    #pprint(the_main_class)





if __name__ == '__main__':
    main()