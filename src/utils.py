from datetime import datetime
from typing import List

import arrow
import requests
from bs4 import BeautifulSoup
from furl import furl


def get_news_id(url: str) -> int:
    '''
    Get the URL of the article and return an article id
    Currently it takes the 9-digits number at the end of the URL
    Eg: link.com/path/a_news-123456789 -> return 123456789
    '''
    f = furl(url)
    # Get the URL path and remove the extra stuff.
    # If the path ends with an "/", the function path.segments will
    # add a blank item at the end of the list. Remove it to be sure
    # that the last element is the one with the "id"
    path: List[str] = f.path.segments
    path: List[str] = [i for i in path if i != '']
    article_id: int = int(path[-1].split('-')[-1])
    return article_id


def convert_date(date: str) -> datetime:
    '''Convert the input string to a valid Arrow object. Also convert the time to UTC'''
    date = arrow.get(date, 'ddd, DD MMM YYYY HH:mm:ss Z')
    return date.to('utc').naive


def scrape_article(link: str) -> str:
    '''Get all the data about the articles'''
    r = requests.get(link).content
    soup = BeautifulSoup(r, features='html.parser')
    # The article contains some link to other news inside <section> tags. Remove them
    [tag.decompose() for tag in soup.find_all(
        'section', attrs={'class': 'inline-article'})]
    title: str = (soup.find('h1', attrs={'class': 'story__title'})
                      .get_text(strip=True))
    summary: str = (soup.find('div', attrs={'class': 'story__summary'})
                        .get_text(strip=True))
    content: str = (soup.find('div', attrs={'class': 'story__text'})
                        .get_text(strip=True))
    return title, summary, content


def parse(post) -> List[str]:
    link: str = post.link
    pub_date = convert_date(post.published)
    article_id: int = get_news_id(post.link)
    title, summary, content = scrape_article(link=link)
    return article_id, pub_date, link, title, summary, content


def check_diff(id: int) -> None:
    pass
