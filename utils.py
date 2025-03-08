from typing import List
from collections.abc import Callable

def timing(func: Callable):
    """Timing function"""
    
    import time
    
    def wrapper():
        tic = time.perf_counter()
        func()
        print(f'Function {func.__name__} took {(time.perf_counter()-tic)}s')

    return wrapper

def read(file_name: str, delimiter: str = '|', split=True) -> List[str]:
    """Read file, split vocab by delimiter, and return as a list of vocabulary"""

    with open(file_name, 'r', encoding='utf-8') as f:
        raw = f.read()

    vocabs_list = [vocab for vocab in raw.split("\n") if len(vocab) > 0]
    if not split:
        return vocabs_list

    return [vocab.split(delimiter)[0].lower().strip()
            for vocab in vocabs_list]

def find_duplicate(file_name: str) -> List[str]:
    """Find duplicate vocabulary in file, return as a list of vocabulary"""
    
    from collections import Counter
    
    counter = Counter(read(file_name))
    return [word for word, count in counter.items() if count > 1]

def clear_file(file_name: str) -> None:
    open(file_name, 'w').close()

if __name__ == '__main__':
    # Mispelling processing
    # import cambridge
    # data = read('mispelling.txt')
    # for i in range(0, len(data), 2):
    #     print(f'{data[i]} - {data[i+1]}, \
    #           {cambridge.crawl(data[i])} - {cambridge.crawl(data[i+1])}')

    # data = read('phrasal_verb.txt')
    print(find_duplicate('phrasal_verb.txt'))
    pass