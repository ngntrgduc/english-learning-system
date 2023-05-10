def read(file_name='vocabs.txt', delimiter='|'):
    with open(file_name, 'r', encoding='utf-8') as f:
        raw = f.read()
    f.close()
    words_list = [word for word in raw.split("\n") if len(word) > 0]
    return [word.split(delimiter)[0].lower().rstrip()
            for word in words_list]