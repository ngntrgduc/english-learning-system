"""Standalone. Find synonyms of vocab on Thesaurus.com"""
import requests
from rich import print
from rich.panel import Panel
from rich.columns import Columns
from rich.align import Align
from bs4 import BeautifulSoup

def get_url(vocab):
    return f"https://www.thesaurus.com/browse/{vocab.replace(' ', '%20')}"

def find(vocab):
    """Find synonyms of vocab on Thesaurus.com"""
    print(Align.center(Panel(f'Synonyms for [cyan]{vocab}[/]'), vertical='middle'))
    
    url = get_url(vocab)    
    colors = {
        'css-1kg1yv8 eh475bn0': 'red', 
        'css-1gyuw4i eh475bn0': 'orange1',
        'css-1n6g4vv eh475bn0': 'yellow'
    }

    for relevant in colors:
        synonyms = BeautifulSoup(requests.get(url).content, 'lxml') \
                                .find_all(attrs={'class': relevant})
        vocabs = [f'[{colors[relevant]}]{vocab.text.strip()}[/]' for vocab in synonyms]
        if vocabs:
            print(Panel(Columns(vocabs, equal=True, expand=True)))
    
    pass
