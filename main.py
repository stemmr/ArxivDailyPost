import urllib, urllib.request
import feedparser

base_url = 'http://export.arxiv.org/api/query?'

search_query = 'all:electron'
start = 0
max_results = 5
query = f"search_query={search_query}&start={start}&max_results={max_results}"

response = urllib.request.urlopen(base_url + query)
feed = feedparser.parse(response)

if __name__ == '__main__':
    for entry in feed.entries:
        print("---------------")
        print(entry.summary)
        print("---------------")