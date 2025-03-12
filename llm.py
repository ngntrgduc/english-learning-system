import os
import click
from dotenv import load_dotenv
from google import genai
from rich import print as rprint

from utils.print import print_vocabs, print_console, text_red

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=GEMINI_API_KEY)
model = 'gemini-2.0-flash'

def is_valid_obj(obj: dict) -> bool:
    """Check before perform API calling."""
    if obj['print']:
        print_vocabs(obj['data'])
        obj['print'] = False
    
    if len(obj['data']) == obj['original_length']:
        print('No vocabs were given.')
        return False

    return True

@click.command()
@click.pass_obj
def llm(obj) -> None:
    """Definition, word form, and sentences with given vocabs."""
    if not is_valid_obj(obj):
        return
    
    if len(obj['data']) > 5:
        rprint(text_red('The number of vocab is large (>5) for this command, '), end='')
        print('continue? [y/N]:')
        answer = input()
        if answer.lower() == 'n':
            return
        if answer.lower() != 'y':
            return
    
    response = client.models.generate_content(
        model=model, 
        contents=f"""{obj['data']}

        With this given list of vocabulary, provide with grammartically correct: 
        - the definition with its word form in parentheses ()
        - 3 sentences using it
    
        Also wrap the given vocabulary in the result with square bracket, bold and italic format (***). 
        Remember not to response with irrelevant information.
        """
    )
    print_console(response.text)

@click.command('prompt')
@click.argument('prompt', type=str, default='')
@click.pass_obj
def prompt_command(obj, prompt) -> None:
    """Prompt whatever you want."""
    if not prompt:
        prompt = input('user> ')

    if obj['print']:
        print_vocabs(obj['data'])
        obj['print'] = False

    if len(obj['data']) == obj['original_length']:
        content = prompt
    else:
        content = f'{obj['data']}\n{prompt}'

    response = client.models.generate_content(
        model=model, 
        contents=content
    )
    print_console(response.text)

@click.command()
@click.pass_obj
def definition(obj) -> None:
    """Get definition of vocab."""
    if not is_valid_obj(obj):
        return

    response = client.models.generate_content(
        model=model, 
        contents=f"""{obj['data']},
        With given vocabs, provide English definition and word form next to the word, in parentheses"""
    )
    print_console(response.text)