from rich import print

def text_blue(text: str) -> str:
    """Return blue format in rich library."""
    return f'[blue]{text}[/blue]'

def text_red(text: str) -> str:
    """Return red format in rich library."""
    return f'[red]{text}[/red]'

def print_vocabs(vocabs: list[str]) -> None:
    """Print vocabs with link to Cambridge dictionary"""
    if not isinstance(vocabs, list):
        raise ValueError('Require list of vocabs')

    def format(vocab: str) -> str:
        return vocab.strip().replace(' ', '-')
    
    url = 'https://dictionary.cambridge.org/dictionary/english/'
    for vocab in vocabs:
        print(f' - [link={url}{format(vocab)}]{vocab}[/link]')