import requests
from bs4 import BeautifulSoup


def scrape_article(link: str) -> str:
    '''Get all the data about the articles'''
    r = requests.get(link).content
    soup = BeautifulSoup(r, features='html.parser')

    # The article contains some link to other news inside <section> tags. Remove them
    [tag.decompose() for tag in soup.find_all('section', attrs={'class':'inline-article'})]

    title: str = soup.find('h1', attrs={'class':'story__title'}).get_text(strip=True)
    summary: str = soup.find('div', attrs={'class':'story__summary'}).get_text(strip=True)
    content: str = soup.find('div', attrs={'class':'story__text'}).get_text(strip=True)

    return title, summary, content
