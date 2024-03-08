"""Format the export result from Quizlet"""

from utils import read

file_name = 'quizlet'
vocabs_list = read(f'{file_name}.txt', split=False)

with open(f'{file_name}.result.txt', 'w', encoding='utf-8') as f:
    for vocab in vocabs_list:
        f.write(f'{vocab.split(" - ")[0]}\n')

# print(vocabs_list)