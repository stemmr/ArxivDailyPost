import urllib, urllib.request
from datetime import datetime, timedelta
import feedparser
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Paper:
    title: str
    authors: List[str]
    publish_date: str
    abstract: str
    latex: Optional[str] = None
    url: Optional[str] = None

class PaperManager:
    arxiv_base_url = 'http://export.arxiv.org/api/query?'

    def __init__(self):
        # Which embeddings to use
        pass

    def daily_paper(self) -> List[Paper]:
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        start_date = yesterday.strftime("%Y%m%d")
        end_date = today.strftime("%Y%m%d")

        search_query = f'cat:cs.* AND submittedDate:[{start_date} TO {end_date}]'
        start = 0
        # Max allowed results per query. Unlikely there will be a day with this papers published.
        max_results=10000
        query = f"search_query={urllib.parse.quote(search_query)}&start={start}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"

        results = []
        # Paginated retrieval of papers
        query = f"search_query={urllib.parse.quote(search_query)}&start={start}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
        response = urllib.request.urlopen(self.arxiv_base_url + query)
        feed = feedparser.parse(response)
        
        papers = []
        for paper in feed.entries:
            papers.append(Paper(
                    title=paper.title,
                    authors=[auth['name'] for auth in paper.authors],
                    publish_date=paper.published,
                    abstract=paper.summary,
                    latex=None,
                    url = paper.link
                ))
        
        return papers

    def paper_embeddings(self, papers: List[Paper]):
        pass