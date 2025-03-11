from random import sample
import click
from rich import print
import re

from rich_format import text_blue, text_red

data_folder = 'data'
vocabs_file_name = 'vocabs.txt'
vocabs_file_path = f'{data_folder}/{vocabs_file_name}'
with open(vocabs_file_path, 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

vocab_length = len(data)

def write(file_name: str, data: list[str]) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('\n'.join(data))

# changes the default parameters to -h and --help instead of just --help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(
    context_settings=CONTEXT_SETTINGS, 
    invoke_without_command=True, 
    no_args_is_help=True, 
    # chain=True,
)
# @click.pass_context
# def main(ctx):
def main():
    # ctx.ensure_object(dict)
    # ctx.obj.setdefault('data', data)
    return

def print_vocabs(vocabs: list[str]) -> None:
    """Print vocabs with link to Cambridge dictionary"""
    if not isinstance(vocabs, list):
        raise ValueError('Require list of vocabs')

    def format(vocab: str) -> str:
        return vocab.strip().replace(' ', '-')
    
    url = 'https://dictionary.cambridge.org/dictionary/english/'
    for vocab in vocabs:
        print(f' - [link={url}{format(vocab)}]{vocab}[/link]')

def check_valid_range(number: int) -> None:
    if number < 1 or number > vocab_length:
        raise ValueError('Invalid number')

def is_valid_vocab(vocab: str) -> bool:
    if re.findall(r'[^\sa-zA-Z]', vocab):
        print(f' - Invalid vocab: {text_red(vocab)}')
        return False
    
    return True

@main.command()
@click.argument('number', type=int, default=5)
def random( number: int) -> None:
    """Get random vocabs. Default: 5 vocabs."""
    check_valid_range(number)
    print_vocabs(sample(data, number))
    # obj['data'] = sample(data, number)

@main.command()
def check() -> None:
    """Check vocabs file."""
    
    print('Checking duplicated vocabs...')
    s = set()
    has_duplicated = False
    for vocab in data:
        if vocab in s:
            has_duplicated = True
            print(f' - {vocab}')
        s.add(vocab)

    if not has_duplicated:
        print(' - No duplicated vocabs.')

    print('Checking invalid vocabs...')
    has_invalid = False
    for vocab in data:
        if vocab[0].isupper():
            print(f' - Invalid vocab: {vocab}')
            has_invalid = True
        
    if not has_invalid:
        print(' - No invalid vocabs.')

@main.command()
@click.argument('vocab', type=str)
def add(vocab: str) -> None:
    """Add a vocab to file."""
    if not is_valid_vocab(vocab):
        return

    if vocab in data:
        print(f' - {text_blue(vocab)} already exists in {vocabs_file_path}.')
        return
    
    vocab = vocab.strip().lower()
    with open(vocabs_file_path, 'a', encoding='utf-8') as f:
        f.write(f'{vocab}\n')
        print(f' - Added {text_blue(vocab)} to {vocabs_file_path}')

@main.command()
def stat() -> None:
    """Provide statistics."""
    print(f' - Total vocabs: {vocab_length}')

@main.command()
@click.argument('character', type=str)
def char(character: str) -> None:
    """Print all vocabs start with a character."""
    assert len(character) == 1, 'Invalid character'
    assert character.isalpha(), 'Character must be in the alphabet'

    character = character.lower()
    list_vocabs = [vocab for vocab in data if vocab.lower().startswith(character)]
    if not list_vocabs:
        print(f' - There are no vocabs started with {text_blue(character)}')
    else:
        print_vocabs(sorted(list_vocabs))

@main.command()
def delete(vocab: str) -> None:
    """Delete a vocab in file."""
    if vocab in data:
        data.remove(vocab)
    else:
        print(f"Couldn't find {vocab} in file.")

@main.command()
@click.argument('number', type=int, default=5)
# @click.pass_obj
# def head(obj, number: int) -> None:
def head(number: int) -> None:
    """'head' functionality"""
    check_valid_range(number)
    print_vocabs(data[:number])

    # ctx.obj['data'] = ctx.obj['data'][:number]
    # print_vocabs(ctx.obj['filtered_data'])

@main.command()
@click.argument('number', type=int, default=5)
# @click.pass_obj
# def tail(obj, number: int) -> None:
def tail(number: int) -> None:
    """'tail' functionality"""
    check_valid_range(number)
    print_vocabs(data[-number:])

    # ctx.obj['data'] = ctx.obj['data'][-number:]
    # print_vocabs(ctx.obj['data'])


# @main.result_callback()
# @click.pass_context
# def print_results(ctx, result, *args, **kwargs) -> None:
#     if ctx.obj['data'] == data:
#         return
#     else:
#         print_vocabs(ctx.obj['data'])

if __name__ == '__main__':
    main()
