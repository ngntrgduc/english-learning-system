with open('words.txt', 'r', encoding='utf-8') as f:
    raw = f.read()
f.close()

def split_word(words_list, delimiter='|'):
    return [word.split(delimiter)[0].lower().rstrip()
            for word in words_list]

words_list = [word for word in raw.split("\n") if len(word) > 0]
print(split_word(words_list))