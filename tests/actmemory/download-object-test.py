from bs4 import BeautifulSoup

def get_html_from_url(url):
    return html_soup

def get_digital_object_url(soup):
    return digital_object_url

def download_object(url, destination):
    return filename

with open("urls.txt", "r") as f:
    urls = f.read_lines()
    for url in urls:
        soup = get_html_from_url(url)
        object_url = get_digital_object_url(soup)
        download_object(object_url, "pdfs")