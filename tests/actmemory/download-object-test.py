from bs4 import BeautifulSoup
import requests
import time

def get_html_from_url(url):
    # requests library to download html given a url
    url = url.strip()
    #print('url in func', url)
    html = requests.get(url).text
    #print(html)
    # parse
    soup = BeautifulSoup(html)
    return soup

def get_digital_object_url(soup):
    print(soup)
    obj = soup.find("div", {"class": "digital-object-reference"})
    print('obj url', obj.a["href"])
    return obj.a["href"]

def download_object(url, destination):
    # requests library to download pdf to file
    filename = url.split('/')[-1]
    print('filename',filename)
    r = requests.get(url)
    open(filename, 'wb').write(r.content)
    return filename

print('starting download')
with open("tests/actmemory/urls.txt", "r") as f:
    for url in f.readlines():
        print('url', url)
        soup = get_html_from_url(url)
        object_url = get_digital_object_url(soup)
        print(object_url)
        download_object(object_url, "{}/pdfs".format(url.split('/')[-1]))
        time.sleep(5)