import requests
from bs4 import BeautifulSoup

finalResult = r'D:\code\python\crawler\crawlResult.txt'

def trade_spider(max_pages):
    page = 2
    while page <= max_pages:
        if(page == 0):
            page = ''
        else:
            page = str(page)

        url = r'http://www.kijiji.ca/b-autos-camions/laval-rive-nord/2007__/page-'+ page + r'/c174l1700278a68r500.0?ad=offering&price=2000__6000&address=montreal&ll=45.501689,-73.567256&kilometres=20000__60000&a-vendre-par=ownr'
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
    fileResult.write('#################################################'+ r'\n')
    for title in soup.findAll('span',{'itemprop':'name'}):
        fileResult.write(title.string + r'\n')

    table = soup.find('table',{'class':'ad-attributes'})
    #plain_text_table = table.text
    for row in table.findAll("tr"):
        showth = row.find('th')
        showtd = row.find('td')
        if(showth is not None and showtd is not None):
            fileResult.write(showth.text + ':' + showtd.text + r'\n')

    for item_name in soup.findAll('div',{'id':'dv_brochure_template_comments'}):
        if(item_name is not None):
            fileResult.write(item_name.text)
            fileResult.write('#################################################' + r'\n')



fileResult = open(finalResult, 'w',encoding='utf-8')
trade_spider(3)
fileResult.close()
