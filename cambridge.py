import re
import requests
from bs4 import BeautifulSoup

def crawl(vocab):
    """Crawl pronounce of vocabulary from Cambridge dictionary"""

    url = f'https://dictionary.cambridge.org/dictionary/english/{vocab}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    }
    soup = requests.get(url, headers=headers).content
    page = BeautifulSoup(soup, 'lxml')

    pronounce = [re.findall('\/.*\/', str(pron.text))[0] for pron in 
                page.find_all(attrs={'class': 'pron dpron'})]
    # pronounce = f'UK: {pronounce[0]}\nUS: {pronounce[1]}' // UK and US pronounce
    pronounce = pronounce[0] # just UK pronounce
    data = {
        "Name": {"title": [{"text": {"content": vocab}}]},
        "Pronounce": {"rich_text": [{"text": {"content": pronounce}}]}
    }
    
    return data
