from collections import Counter
import re

from .print import text_red

def find_duplicate(list_vocab: list[str]) -> list[str]:
    """Find duplicate vocabulary, return as a list of vocabulary"""
    counter = Counter(list_vocab)
    return [word for word, count in counter.items() if count > 1]

def is_valid_vocab(vocab: str) -> bool:
    """Check if a vocab is valid"""
    assert isinstance(vocab, str), 'Vocabulary must be a string'
    if re.findall(r'[^\sa-zA-Z]', vocab):
        print(f' - Invalid vocab: {text_red(vocab)}')
        return False
    
    return True