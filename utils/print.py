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
        vocabs = [vocabs]

    if not isinstance(vocabs, list):
        raise ValueError('Require list of vocabs')

    vocabs = [link(vocab) for vocab in vocabs]

    if len(vocabs) >= 10:
        from rich.columns import Columns
        from rich.console import Console
        console = Console(width=80)
        console.print(Columns(vocabs, equal=True, expand=True))
    else:
        from rich import print
        for vocab in vocabs:
            print(vocab)

def print_console(text: str) -> None:
    """Print markdown format to console, used for llm response"""
    from rich.console import Console
    from rich.markdown import Markdown
    
    console = Console(width=90)
    console.rule()
    console.print(Markdown(text))
    console.rule()
