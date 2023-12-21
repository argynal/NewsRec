# news/rss_parser.py
import feedparser

def parse_rss(url):
    feed = feedparser.parse(url)
    news_list = []
    for entry in feed.entries:
        news = {
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary,
            'published': entry.published,
            'category': entry.category
        }
        news_list.append(news)
    return news_list
