from typing import List
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
