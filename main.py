import urllib, urllib.request
from datetime import datetime, timedelta
import feedparser

from papers import PaperManager

if __name__ == '__main__':
    manager = PaperManager()
    papers = manager.daily_paper()
    print(len(papers))
    print(manager.paper_embeddings(papers))