from bs4 import BeautifulSoup
import requests,re

def get_cities(website):
    page = requests.get(website)
    print page
    print '###########################'
    page_info = BeautifulSoup(page.text)


    for cell in page_info.find_all('tr'):
        words = cell.get_text()
        city_loc = re.sub(r'\d+:\d+.+', '', words)
        print city_loc
        print '---------------------------------'

    print '================================='
    # data = coord.text
    # book_text = BeautifulSoup(data)
    # for paragraph in book_text.find_all(""):
    #     words = paragraph.get_text()
