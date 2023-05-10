def read(file_name='vocabs.txt', delimiter='|'):
    with open(file_name, 'r', encoding='utf-8') as f:
        raw = f.read()
    f.close()
    vocabs_list = [vocab for vocab in raw.split("\n") if len(vocab) > 0]
    return [vocab.split(delimiter)[0].lower().rstrip()
            for vocab in vocabs_list]