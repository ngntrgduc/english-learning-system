def timing(func):
    """Output time taken of function"""
    from functools import wraps
    from time import perf_counter

    @wraps(func)
    def wrapper(*args, **kwargs):
        tic = perf_counter()
        result = func(*args, **kwargs)
        print(f' - {func.__name__}() took {perf_counter() - tic}s')
        return result

    return wrapper

def read(file_name: str, split=False, delimiter: str = '|') -> list[str]:
    """Read file, split vocab by delimiter, and return as a list of vocabulary"""

    with open(file_name, 'r', encoding='utf-8') as f:
        raw = f.read()

    vocabs_list = [vocab for vocab in raw.split('\n') if len(vocab) > 0]
    if not split:
        return vocabs_list

    return [vocab.split(delimiter)[0].lower().strip()
            for vocab in vocabs_list]

def clear_file(file_name: str) -> None:
    open(file_name, 'w').close()

if __name__ == '__main__':
    pass