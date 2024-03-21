import urllib, urllib.request
from datetime import datetime, timedelta
import feedparser

base_url = 'http://export.arxiv.org/api/query?'

today = datetime.now().date()
yesterday = today - timedelta(days=1)
start_date = yesterday.strftime("%Y%m%d")
end_date = today.strftime("%Y%m%d")

search_query = f'cat:cs.* AND submittedDate:[{start_date} TO {end_date}]'
start = 0
max_results = 10  # Adjust the number of results as needed
query = f"search_query={urllib.parse.quote(search_query)}&start={start}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"

response = urllib.request.urlopen(base_url + query)
feed = feedparser.parse(response)

total_results = feed.feed.opensearch_totalresults

if __name__ == '__main__':
    print(f"Over the past 24 Hours, {total_results} Computer Science papers have been published to the ArXiv")
    for entry in feed.entries:
        print("---------------")
        print(entry.summary)
        print("---------------")