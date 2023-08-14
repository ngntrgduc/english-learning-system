import os
import re
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

headers = {
    'User-Agent': os.getenv('USER_AGENT')
}

def crawl(vocab):
    """Crawl and return pronounce of vocabulary from Cambridge dictionary"""
    
    url = f'https://dictionary.cambridge.org/dictionary/english/{vocab}'
    soup = requests.get(url, headers=headers).content
    page = BeautifulSoup(soup, 'lxml')

    pronounces = [re.findall('\/.*\/', str(pron.text))[0] for pron in 
                page.find_all(attrs={'class': 'pron dpron'})]
    # pronounce = f'UK: {pronounces[0]}\nUS: {pronounces[1]}' // UK and US pronounce
    try:
        pronounce = pronounces[0] # just UK pronounce
    except:
        print(f'* Cannot get pronounce of {vocab}')
    
    return pronounce
