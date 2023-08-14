import time
import random
import cambridge
from tqdm import tqdm
from rich import print
from utils.vocabs import read
from utils.tictoc import timing

def clear_file(file):
    """Clear vocabs file"""
    open(file, 'w').close()
    pass

@timing
def main():
    vocabs_file = 'vocabs.txt'
    vocabs = read(vocabs_file)
    with open('result.txt', 'w', encoding='utf-8' ) as f:
        for vocab in tqdm(vocabs, desc='Crawl & create', unit='word'):
            time.sleep(random.random() + 1)
            pronounce = cambridge.crawl(vocab)
            f.write(f'{vocab},{pronounce}\n')
    f.close()
    clear_file(vocabs_file)

main()