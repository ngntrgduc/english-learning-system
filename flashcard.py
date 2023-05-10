import json
from rich import print

def get_vocab():
    data = json.load(open('vocabs.json', 'r', encoding='utf-8'))
    for i in range(len(data['results'])):
        vocab = data['results'][i]['properties']['Name']['title'][0]['plain_text']
        meaning = ''
        for piece in data['results'][i]['properties']['Meaning']['rich_text']:
            meaning += piece['plain_text'].replace(u'\xa0', u' ').replace('\n', ' | ')
        print(f'- [cyan]{vocab}[/]: {meaning}\n')
    pass

get_vocab()