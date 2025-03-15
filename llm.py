import click

# https://ai.google.dev/gemini-api/docs/models/gemini
model = 'gemini-2.0-flash'

def get_api_key() -> str:
    from os import getenv
    from dotenv import load_dotenv
    
    load_dotenv()
    return getenv('GEMINI_API_KEY')

def is_valid_obj(obj: dict) -> bool:
    """Check before perform API calling."""
    from utils.print import print_vocabs

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
    from google import genai
    from utils.print import print_console

    if not is_valid_obj(obj):
        return
    
    if len(obj['data']) > 5:
        print('The number of vocab is large (>5) for this command, continue? [y/N]:')
        answer = input()
        if answer.lower() == 'n':
            return
        if answer.lower() != 'y':
            return
    
    GEMINI_API_KEY = get_api_key()
    client = genai.Client(api_key=GEMINI_API_KEY)
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
    from google import genai
    from utils.print import print_vocabs, print_console

    if not prompt:
        prompt = input('user> ')

    if obj['print']:
        print_vocabs(obj['data'])
        obj['print'] = False

    if len(obj['data']) == obj['original_length']:
        content = prompt
    else:
        content = f'{obj['data']}\n{prompt}'

    GEMINI_API_KEY = get_api_key()
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model=model, 
        contents=content
    )
    print_console(response.text)

@click.command()
@click.pass_obj
def definition(obj) -> None:
    """Get definition of vocab."""
    from google import genai
    from utils.print import print_console

    if not is_valid_obj(obj):
        return

    GEMINI_API_KEY = get_api_key()
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model=model, 
        contents=f"""{obj['data']},
        With given vocabs, provide English definition and word form next to the word, in parentheses"""
    )
    print_console(response.text)

@click.command()
@click.pass_obj
def paragraph(obj) -> None:
    """Generate a paragraph with given vocab."""
    from google import genai
    from utils.print import print_console

    if not is_valid_obj(obj):
        return

    GEMINI_API_KEY = get_api_key()
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model=model, 
        contents=f"""{obj['data']},
        With given vocabs, provide a paragraph contain all the vocabs in it, with best coherence.
        Also wrap the given vocabulary in the result with square bracket, bold and italic format (***). 
        Remember not to response with irrelevant information."""
    )
    print_console(response.text)