# Crawl vocabulary database on Notion, find missing pronounce and update
import os
import dotenv
import time
import json
import random
import notion
import cambridge
from rich import print
from utils.tictoc import timing

def crawl():
    dotenv.load_dotenv()
    VOCAB_DATABASE_ID = os.getenv('VOCAB_DATABASE_ID')
    data = notion.read_database(VOCAB_DATABASE_ID)
    with open('vocabs.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    f.close()
    pass

def get_missing_pronounce():
    vocabs = ()
    data = json.load(open('vocabs.json', 'r', encoding='utf-8'))
    for i in range(len(data['results'])):
        pronounce = data['results'][i]['properties']['Pronounce']['rich_text']
        if not pronounce:
            word = data['results'][i]['properties']['Name']['title'][0]['plain_text']
            vocabs = vocabs + (word,)
    return vocabs

def update_pronounce(missing):
    data = json.load(open('vocabs.json', 'r', encoding='utf-8'))
    for i in range(len(data['results'])):
        vocab = data['results'][i]['properties']['Name']['title'][0]['plain_text']
        if vocab in missing:
            print(f'- Update pronounce for "{vocab}"')
            page_id = data['results'][i]['id']
            time.sleep(random.random()*1 + 1) # avoid blocking
            try:
                notion.update(page_id, cambridge.crawl(vocab))
            except:
                continue
    pass
        
@timing
def main():
    crawl()
    missing = get_missing_pronounce()
    update_pronounce(missing)
    pass

main()