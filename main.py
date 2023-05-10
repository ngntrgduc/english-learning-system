import cambridge
import notion
import thesaurus

from rich import print
import random
import time

def split_word(words_list, delimiter=' '):
    return [word.split(delimiter)[0].lower()
            for word in words_list]

# file = 'words.txt'
# # file = 'misspelling.txt'
# with open(file, 'r', encoding='utf-8') as f:
#     raw = f.read()
# f.close()
# words_list = [word.strip() for word in raw.split("\n") 
#               if len(word.strip()) > 0]
# words = split_word(words_list, '|')
# # print(words)

# for word in words:
    # time.sleep(random.random()*1 + 1)
    
    # data = cambridge.crawl(word)
    # print(data)
    # notion.create(data)
    # thesaurus.find(word)
