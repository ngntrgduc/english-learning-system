# English-learning-system
Not actually a learning system. Just some small scripts to help me learn English efficiently (maybe).

## Roadmap
At first, I used Notion to store vocabulary as a database, grammar, writing tips, and speaking samples as pages. I coded the [pronunciation crawling feature](/deprecated/cambridge.py) from Cambridge Dictionary, then used Notion's database API to push the data to the vocabulary database.
I also coded the [antonym/synonym crawling](/deprecated/thesaurus.py) from [Thesaurus.com](https://www.thesaurus.com/), and beautified the result in the console using `rich` library.

Then, I realized Notion is too laggy for me when the database is large, not for the long run. 
So I switched to [Anki](https://apps.ankiweb.net/), taking the advantage of Space repetition method. I [crawled vocab pronunciations](/deprecated/main.py) (reduced crawling time using `asyncio`), and imported it to Anki with [my custom Anki template](/anki_template.html). 

But since I watched [this video](https://www.youtube.com/watch?v=--Hu2w0s72Y), I decided to take a different approach.

**Now**: I've been working on the CLI + LLM ([Gemini](https://ai.google.dev/gemini-api/docs)) version...

## Structure
- `el.py`: CLI tool to learn English
- `ludwigy.py` [***WIP***]: Act like [Ludwig.guru](https://app.ludwig.guru/), no limitation
- `utils/`: Timing code, Read and format vocabs from raw file, Clear file, Find duplicate vocabs, Format vocab

Folder `deprecated/` contains some deprecated/old scripts:
- `notion/`: Interact with Notion database using API, not sure if the code still works
- `cambridge.py`: Crawl pronunciation of vocabulary from Crambridge Dictionary
- `logger.py`: Log information to `runtime.log`
- `main.py`: Crawl the pronunciation of vocabs from a file and write the results to a file for import into Anki
- `quizlet.py`: Small script to format the exported result from Quizlet
- `thesaurus.py`: Crawl synonyms of vocab on https://www.thesaurus.com/

## How to use
- Install dependencies:
    - Python libraries
        ```py
        pip install rich click dotenv google-genai
        ```
    - [fzf](https://github.com/junegunn/fzf)
- [Create Gemini API key](https://ai.google.dev/gemini-api/docs/api-key)
- Create `.env` file and store your API key with format: **`GEMINI_API_KEY = '<your_api_key>'`**

```
 py el.py
Usage: el.py [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -h, --help  Show this message and exit.

Commands:
  add         Add a vocab to file.
  check       Check vocab file.
  definition  Get definition of vocab.
  delete      Delete a vocab using fzf.
  find        Find vocabs using fzf.
  head        'head' functionality.
  llm         Definition, word form, and sentences with given vocabs.
  paragraph   Generate a paragraph with given vocab.
  prompt      Prompt whatever you want.
  random      Get random vocabs.
  start       List all vocabs start with some character.
  stat        Show vocab statistics.
  tail        'tail' functionality.
```

## TODO
- [ ] Create a chatbot for writing skills, checking grammar...
    - [ ] find a model specific for english learning, or finetune it...
- [ ] Convert to database? does it faster?
- [x] Rewrite it to CLI using Click 
    - [x] Integrate fzf
    - [ ] convert it to a module? with `uv` for faster installation
    - [ ] split commands into different files
    - [ ] ~~implement trie with auto suggestion instead of fzf?~~ -> Overengineering, fzf already did this
    - [ ] REPL mode?
    - [x] LLM to generate sentence/paragraph for given vocab
        - [x] Call Gemini API?
    - [ ] Lazy loading to improve performance
        - [ ] https://click.palletsprojects.com/en/stable/complex/#lazily-loading-subcommands
    - [x] Automatically display vocabs as clumns
    - [ ] Add GIF to demo the workflow
    - [ ] Handle multiple llm commands

## Some good resources 🔥
- [IELTS Online Tests](https://ieltsonlinetests.com/ielts-exam-library#academic-test)
- [Dictionary Look Up](https://github.com/ngntrgduc/Dictionary-Look-Up): Browser extension for quickly look up for vocabs.
- [The Best (and Worst) IELTS Websites - TED IELTS](https://ted-ielts.com/ielts-website-review/)

For Vietnamese:
- https://www.tuhocielts.online/
- https://study4.com/
- https://zim.vn/bai-viet

### Happy learning 🐧