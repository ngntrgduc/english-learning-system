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
- Create `.env` file and store your API key

```
> py el.py
Usage: el.py [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -h, --help  Show this message and exit.

Commands:
  add     Add a vocab to file.
  char    Print all vocabs start with a character.
  check   Check vocab file.
  delete  Delete a vocab in file.
  head    'head' functionality.
  llm     Cenerate sentences/paragraphs with given vocab, using Gemini
  random  Get random vocabs.
  stat    Show vocab statistics.
  tail    'tail' functionality.
```

## TODO
- [ ] Create a chatbot for writing skills, checking grammar...
    - [ ] Mistral? find model specific for english learning, or finetune it...
- [ ] Convert to database? does it faster?
- [x] Rewrite it to CLI using Click 
    - [x] Integrate fzf
    - [ ] convert it to a module?
    - [ ] implement trie with auto suggestion instead of fzf?
    - [ ] REPL mode?
    - [x] LLM to generate sentence/paragraph for given vocab
        - [x] Call Gemini API?
    - [ ] chat interface?

## Some good resources 🔥
- [IELTS Online Tests](https://ieltsonlinetests.com/ielts-exam-library#academic-test)
- [Dictionary Look Up](https://github.com/ngntrgduc/Dictionary-Look-Up): Browser extension for quickly look up for vocabs.
- [The Best (and Worst) IELTS Websites - TED IELTS](https://ted-ielts.com/ielts-website-review/)

For Vietnamese:
- https://www.tuhocielts.online/
- https://study4.com/

### Happy learning 🐧