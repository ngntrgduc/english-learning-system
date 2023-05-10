import time
import notion
import random
import cambridge
from rich import print
from utils.words import read
from utils.tictoc import timing
from pronounce import update_pronounce

def clear_file(file):
    open(file, 'w').close()
    pass

@timing
def main():
    file = 'vocabs.txt'
    vocabs = read(file)
    for vocab in vocabs:
        print(f'- {vocab}')
        time.sleep(random.random() + 1)    
        notion.create(cambridge.crawl(vocab))

    clear_file(file)    
    update_pronounce()

main()