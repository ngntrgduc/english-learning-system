import click

# https://ai.google.dev/gemini-api/docs/models/gemini
model = 'gemini-2.0-flash'
INSTRUCT = """Also wrap the given vocabulary in the result with square bracket, 
                bold and italic format ([***<vocab>***]). 
                Remember not to response with irrelevant information."""

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
    if not is_valid_obj(obj):
        return
    
    if len(obj['data']) > 5:
        if not click.confirm('The number of vocab is large (>5) for this command. Do you want to continue?'):
            return
    
    from google import genai
    from utils.print import print_console

    GEMINI_API_KEY = get_api_key()
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model=model, 
        contents=f"""{obj['data']}

        With this given list of vocabulary, provide with grammartically correct: 
        - the definition with its word form in parentheses ()
        - 3 sentences using it
    
        {INSTRUCT}
        """
    )
    print_console(response.text)

@click.command('prompt')
@click.argument('prompt', type=str, default='')
@click.pass_obj
def prompt_command(obj, prompt) -> None:
    """Prompt whatever you want."""
    from utils.print import print_vocabs, print_console
    
    if obj['print']:
        print_vocabs(obj['data'])
        obj['print'] = False
    
    if not prompt:
        prompt = click.prompt('Enter your prompt', type=str)

    if len(obj['data']) == obj['original_length']:
        content = prompt
    else:
        content = f'{obj['data']}\n{prompt}'

    from google import genai

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
    if not is_valid_obj(obj):
        vocab = click.prompt('Enter vocabs', type=str)
        if not vocab:
            return
        obj['data'] = vocab

    from google import genai
    from utils.print import print_console

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
    if not is_valid_obj(obj):
        return

    from google import genai
    from utils.print import print_console

    GEMINI_API_KEY = get_api_key()
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model=model, 
        contents=f"""{obj['data']},
        With given vocabs, provide a paragraph contain all the vocabs in it, with best coherence.
        {INSTRUCT}
        """
    )
    print_console(response.text)