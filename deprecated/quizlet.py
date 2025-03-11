"""Format the exported result from Quizlet"""

from utils import read

file_name = 'quizlet'
vocabs_list = read(f'data/{file_name}.txt', delimiter=' - ', split=True)

with open(f'data/{file_name}.result.txt', 'w', encoding='utf-8') as f:
    for vocab in vocabs_list:
        f.write(f'{vocab}\n')
