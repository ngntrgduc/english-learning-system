def find_duplicate(list_vocab: list[str]) -> list[str]:
    """Find duplicate vocabulary, return as a list of vocabulary"""
    from collections import Counter
    counter = Counter(list_vocab)
    return [word for word, count in counter.items() if count > 1]

def is_valid_vocab(vocab: str) -> bool:
    """Check if a vocab is valid"""
    import re
    from .print import text_red
    
    assert isinstance(vocab, str), 'Vocabulary must be a string'
    if re.findall(r'[^\sa-zA-Z]', vocab):
        print(f' - Invalid vocab: {text_red(vocab)}')
        return False
    
    return True