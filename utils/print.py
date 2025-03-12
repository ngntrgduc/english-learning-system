from rich import print
from rich.console import Console
from rich.markdown import Markdown

def text_blue(text: str) -> str:
    """Return blue format in rich library."""
    return f'[blue]{text}[/blue]'

def text_red(text: str) -> str:
    """Return red format in rich library."""
    return f'[red]{text}[/red]'

def print_vocabs(vocabs: list[str] | str) -> None:
    """Print vocabs with link to Cambridge dictionary"""
    def link(vocab) -> str:
        url = 'https://dictionary.cambridge.org/dictionary/english/'
        return f' - [link={url}{vocab.strip().replace(' ', '-')}]{vocab}[/link]'
    
    if isinstance(vocabs, str):
        print(link(vocabs))
        return

    if not isinstance(vocabs, list):
        raise ValueError('Require list of vocabs')
 
    for vocab in vocabs:
        print(link(vocab))

def print_console(text: str) -> None:
    """Print markdown format to console, used for llm response"""
    console = Console(width=90)
    console.rule()
    console.print(Markdown(text))
    console.rule()