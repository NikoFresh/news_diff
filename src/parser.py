from typing import List, Dict

import feedparser

def parse(link: str) -> List[Dict[str, str]]:
    data = feedparser.parse(link)
    posts = data.entries
    output: List[Dict[str, str]] = []
    for post in posts:
        temp: Dict[str, str] = {}
        temp['title'] = post.title
        temp['link'] = post.link
        temp['author'] = post.author
        temp['pubDate'] = post.published
        temp['description'] = post.description
        output.append(temp)
    return output