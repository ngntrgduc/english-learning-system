from random import sample
import click
from rich import print
from rich.console import Console
from rich.markdown import Markdown

from utils.print import text_blue, text_red, print_vocabs
from utils.vocab import find_duplicate, is_valid_vocab

data_folder = 'data'
vocabs_file_name = 'vocabs.txt'
vocabs_file_path = f'{data_folder}/{vocabs_file_name}'
with open(vocabs_file_path, 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

vocab_length = len(data)

# changes the default parameters to -h and --help instead of just --help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(
    context_settings=CONTEXT_SETTINGS, 
    invoke_without_command=True, 
    no_args_is_help=True, 
    chain=True,
)
@click.pass_context
def main(ctx):
    ctx.ensure_object(dict)
    ctx.obj.setdefault('data', data)
    ctx.obj.setdefault('print', False)

def check_valid_range(number: int) -> None:
    assert isinstance(number, int), 'Number must be integer'
    if number < 1 or number > vocab_length:
        raise ValueError('Invalid number range.')

@main.command()
@click.argument('number', type=int, default=5)
@click.pass_context
def random(ctx, number: int) -> None:
    """Get random vocabs."""
    check_valid_range(number)
    ctx.obj['data'] = sample(ctx.obj['data'], number)
    ctx.obj['print'] = True

@main.command()
def check() -> None:
    """Check vocab file."""
    print('Checking duplicated vocabs...')
    print(find_duplicate(data))

    print('Checking invalid vocabs...')
    for vocab in data:
        if vocab[0].isupper():
            print(f' - {text_red(vocab)}')
 
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
    """Show vocab statistics."""
    print(f' - Total vocabs: {vocab_length}')

@main.command()
@click.argument('character', type=str)
@click.pass_context
def char(ctx, character: str) -> None:
    """Print all vocabs start with a character."""
    assert len(character) == 1, 'Invalid character'
    assert character.isalpha(), 'Character must be in the alphabet'

    character = character.lower()
    list_vocabs = [vocab for vocab in data if vocab.lower().startswith(character)]
    if not list_vocabs:
        print(f' - There are no vocabs started with {text_blue(character)}')
    else:
        ctx.obj['print'] = True
        ctx.obj['data'] = sorted(list_vocabs)

@main.command()
@click.argument('vocab', type=str)
def delete(vocab: str) -> None:
    """Delete a vocab in file."""
    if vocab in data:
        data.remove(vocab)
        print(f' - Removed {text_blue(vocab)} in {vocabs_file_path}.')
    else:
        print(f" - Couldn't find {text_red(vocab)} in {vocabs_file_path}.")

@main.command()
@click.argument('number', type=int, default=5)
@click.pass_context
def head(ctx, number: int) -> None:
    """'head' functionality."""
    check_valid_range(number)
    ctx.obj['data'] = ctx.obj['data'][:number]
    ctx.obj['print'] = True

@main.command()
@click.argument('number', type=int, default=5)
@click.pass_context
def tail(ctx, number: int) -> None:
    """'tail' functionality."""
    check_valid_range(number)
    ctx.obj['data'] = ctx.obj['data'][-number:]
    ctx.obj['print'] = True

@main.result_callback()
@click.pass_obj
def print_to_console(obj, result, *args, **kwargs) -> None:
    if obj['print']:
        print_vocabs(obj['data'])

@main.command()
@click.pass_obj
def llm(obj) -> None:
    """Cenerate sentences/paragraphs with given vocab, using Gemini"""
    if len(obj['data']) == vocab_length:
        print('No vocab were given.')
        return

    if obj['print']:
        print_vocabs(obj['data'])
        obj['print'] = False

    if len(obj['data']) > 5:
        print(f"{text_red('The number of vocab is large (>5)')}, would you want to continue? [y/N]:")
        answer = input()
        if answer.lower() == 'n':
            return
        if answer.lower() != 'y':
            return

    from google import genai
    import os
    from dotenv import load_dotenv
    load_dotenv()
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model='gemini-2.0-flash', 
        contents=f"""{obj['data']}

        With this given list of vocabulary, provide the definition, word form, 
        and generate 3 sentences using it, with grammartically correct.
        Also wrap the given vocabulary in the result with square bracket, bold and italic format. 
        Remember not to response with irrelevant information.
        """
    )
    console = Console(width=90)
    console.rule()
    console.print(Markdown(response.text))


if __name__ == '__main__':
    main()
