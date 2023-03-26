from rich import print
from rich.panel import Panel
from rich.columns import Columns
from bs4 import BeautifulSoup
import requests

def get_url(word):
    return f"https://www.thesaurus.com/browse/{word.replace(' ', '%20')}"

word = input('Search synonyms for : ')
url = get_url(word)

colors = {
    'css-1kg1yv8 eh475bn0': 'red', 
    'css-1gyuw4i eh475bn0': 'orange1',
    'css-1n6g4vv eh475bn0': 'yellow'
}

for relevant in colors:
    synonyms = BeautifulSoup(requests.get(url).content, 'lxml')\
                            .find_all(attrs={'class': relevant})
    words = [f'[{colors[relevant]}]{word.text.strip()}[/]' for word in synonyms]
    if len(words) > 0:
        print(Panel(Columns(words, equal=True, expand=True)))