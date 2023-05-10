import os
import re
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

def crawl(vocab):
    """Crawl pronounce of vocabulary from Cambridge dictionary, 
    and return to json format for update to database"""
    url = f'https://dictionary.cambridge.org/dictionary/english/{vocab}'
    headers = {
        'User-Agent': os.getenv('USER_AGENT')
    }
    soup = requests.get(url, headers=headers).content
    page = BeautifulSoup(soup, 'lxml')

    pronounce = [re.findall('\/.*\/', str(pron.text))[0] for pron in 
                page.find_all(attrs={'class': 'pron dpron'})]
    # pronounce = f'UK: {pronounce[0]}\nUS: {pronounce[1]}' // UK and US pronounce
    try:
        pronounce = pronounce[0] # just UK pronounce
    except:
        print(f'* Cannot get pronounce of {vocab}')

    data = {
        "Name": {"title": [{"text": {"content": vocab}}]},
        "Pronounce": {"rich_text": [{"text": {"content": pronounce}}]}
    }
    
    return data
