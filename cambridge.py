from bs4 import BeautifulSoup
from rich import print
import requests
import re

from notion import create

def crawl(word):
    url = f'https://dictionary.cambridge.org/dictionary/english/{word}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
    }
    soup = requests.get(url, headers=headers).content
    page = BeautifulSoup(soup, 'lxml')

    # type = page.find_all(attrs={'class': 'pos dpos'})[0].text
    # type = page.find_all(attrs={'class': 'pos dpos'})
    # for i in type: print(i)

    pronounce = [re.findall('\/.*\/', str(pron.text))[0] for pron in 
                page.find_all(attrs={'class': 'pron dpron'})]
    # pronounce = f'UK: {pronounce[0]}\nUS: {pronounce[1]}' // UK and US pronounce
    pronounce = pronounce[0] # just UK pronounce

    # meanings = page.find_all(attrs={'class': 'ddef_h'})
    # meanings = ''.join([f'- {meaning.text.strip()[:-1]}\n' 
    #                    for meaning in meanings
    #                    if len(meaning.text.strip()) > 0])
    # print(meanings)

    # examples = page.find_all(attrs={'class': 'eg deg'})
    # examples = ''.join([f'- {example.text}\n' for example in examples])
    # print(examples)    

    data = {
        "Name": {"title": [{"text": {"content": word}}]},
        "Pronounce": {"rich_text": [{"text": {"content": pronounce}}]}
        # "Type": {"rich_text": [{"text": {"content": type}}]}
        # "Meaning": {"rich_text": [{"text": {"content": meanings}}]},
        # "Example": {"rich_text": [{"text": {"content": examples}}]},
    }
    
    return data

# create(data)

# data = crawl_word('mesmerizing')
# print(data)
