"""Find duplicated vocab from file"""
import notion
import json
import os

def crawl(database_id=os.getenv('VOCAB_DATABASE_ID')):
    """Crawl vocabulary from Notion database and write it to `vocabs.json`"""
    data = notion.read_database(database_id)
    with open('vocabs.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    f.close()
    pass

def find_duplicated():
    """Get missing pronounce vocabulary from file"""
    crawl()
    vocabs = ()
    data = json.load(open('vocabs.json', 'r', encoding='utf-8'))
    for i in range(len(data['results'])):
        vocab = data['results'][i]['properties']['Name']['title'][0]['plain_text']
        vocabs = vocabs + (vocab,)

    duplicated = []
    for vocab in vocabs:
        count = vocabs.count(vocab)
        if count > 1:
            if vocab not in duplicated:
                duplicated.append(vocab)
    return duplicated

print(find_duplicated())