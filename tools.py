import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

def summarize_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    summary = summarize(text, word_count=2000)
    return summary