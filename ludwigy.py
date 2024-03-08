import os
import requests
from dotenv import load_dotenv
from rich import print
from bs4 import BeautifulSoup

load_dotenv()

headers = {
    'User-Agent': os.getenv('USER_AGENT')
}

urls = [
    ''
]
# - The Guardian: https://www.theguardian.com/international
#     - https://www.google.co.uk/search?as_q=&as_epq=albeit&lr=lang_enl&as_sitesearch=www.theguardian.com

# - Quarzt: https://qz.com/
# - The New York Times: 
# - The new yorker: https://www.newyorker.com/
# - ScienceDirect
# - BBC: https://www.bbc.com/
# - unicef:
# - Forbes:
# - Publmed: https://pubmed.ncbi.nlm.nih.gov/
# - CNN: https://edition.cnn.com/
# the economist:
# indepentdent:
# business insider:
# https://techcrunch.com/

# for url in urls:
    # soup = requests.get(url, headers=headers)

word = 'how it going'
word = word.replace(' ', '+')
google_search = f'https://www.google.com/search?q="{word}"'
grammar_check = f'https://www.google.com/search?q={word}+grammar+check'
print(google_search)
print(grammar_check)