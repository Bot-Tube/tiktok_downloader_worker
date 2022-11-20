from bs4 import BeautifulSoup

def parse_response(response):
    soup = BeautifulSoup(response, 'html.parser')
    return soup.prettify()
