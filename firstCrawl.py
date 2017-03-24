import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 2
    while page <= max_pages:
        if(page == 0):
            page = ''
        else:
            page = str(page)
        url = 'http://www.kijiji.ca/b-autos-camions/quebec/page-'+ page + '/c174l9001'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml")
        for link in soup.findAll('a',{'class':'enable-search-navigation-flag'}):
            href = 'http://www.kijiji.ca' + link.get('href')
            # title = link.string
            get_single_item_data(href)

        if(page == ''):
            page = 1
        else:
            page = int(page)
            page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")
    print '#################################################'
    for title in soup.findAll('span',{'itemprop':'name'}):
        print title.string

    table = soup.find('table',{'class':'ad-attributes'})
    rows = list()
    for row in table.findAll("tr"):
        showth = table.find('th')
        showtd = table.find('td')
        print showth
        print showtd

    for item_name in soup.findAll('div',{'id':'dv_brochure_template_comments'}):
        print item_name.string
    print '#################################################'

trade_spider(5)