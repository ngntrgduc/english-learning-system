import notion
import cambridge
import thesaurus

from rich import print
import random
import time

def split_word(words_list, delimiter=' '):
    return [word.split(delimiter)[0].lower().strip()
            for word in words_list]

raw = """
VICIOUS | English meaning - Cambridge Dictionary
INSIDIOUS | English meaning - Cambridge Dictionary
CONCISE | English meaning - Cambridge Dictionary
PRAGMATIC | English meaning - Cambridge Dictionary
INQUISITIVE | English meaning - Cambridge Dictionary
GENUINE | English meaning - Cambridge Dictionary
"""

words_list = [word for word in raw.split("\n") 
              if len(word) > 0]
words = split_word(words_list)
# print(words)

for word in words:
    # time.sleep(random.random()*1 + 1)
    
    data = cambridge.crawl(word)
    # print(data)

    notion.create(data)

    # thesaurus.find(word)