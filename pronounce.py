"""Crawl vocabulary database on Notion and write to file, find missing pronounce and update"""
import os
import dotenv
import time
import json
import random
import notion
import cambridge
from rich import print

dotenv.load_dotenv()

def crawl(database_id=os.getenv('VOCAB_DATABASE_ID')):
    """Crawl vocabulary from Notion database and write it to `vocabs.json`"""
    data = notion.read_database(database_id)
    with open('vocabs.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    f.close()
    pass

def get_missing_pronounce():
    """Get missing pronounce vocabulary from file"""
    crawl()
    vocabs = ()
    data = json.load(open('vocabs.json', 'r', encoding='utf-8'))
    for i in range(len(data['results'])):
        pronounce = data['results'][i]['properties']['Pronounce']['rich_text']
        if not pronounce:
            word = data['results'][i]['properties']['Name']['title'][0]['plain_text']
            vocabs = vocabs + (word,)
    return vocabs

def update_pronounce():
    """Update pronounce to database"""
    missing = get_missing_pronounce()
    data = json.load(open('vocabs.json', 'r', encoding='utf-8'))
    for i in range(len(data['results'])):
        vocab = data['results'][i]['properties']['Name']['title'][0]['plain_text']
        if vocab in missing:
            print(f'- Update pronounce for "{vocab}"')
            page_id = data['results'][i]['id']
            time.sleep(random.random() + 1) # avoid blocking
            try:
                notion.update(page_id, cambridge.crawl(vocab))
            except:
                print(f'- Cannot update for "{vocab}"')
                continue
    pass

update_pronounce() 