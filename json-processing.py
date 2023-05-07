# This program crawl vocabulary database on Notion and format it to easily import to Quizlet
# With setings: 'Tab' between term and definition, `New line` between cards
import json
import notion
from rich import print

def crawl():
    import os
    import dotenv
    dotenv.load_dotenv()
    VOCAB_DATABASE_ID = os.getenv('VOCAB_DATABASE_ID')
    data = notion.read_database(VOCAB_DATABASE_ID)
    with open('vocabs.json', 'r', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

data = json.load(open('vocabs.json', 'r', encoding='utf-8'))
word_col, meaning_col = 'Name', 'Meaning'
with open('vocabs.txt', 'w', encoding='utf-8') as output:
    for i in range(len(data['results'])):
        word = data['results'][i]['properties'][word_col]['title'][0]['plain_text']
        meaning = ''
        for piece in data['results'][i]['properties'][meaning_col]['rich_text']:
            meaning += piece['plain_text'].replace(u'\xa0', u' ').replace('\n', ' | ')
        output.write(f'{word}    {meaning}\n')
