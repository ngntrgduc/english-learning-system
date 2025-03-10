# English-learning-system
My English learning system, with Anki (for now).

## Roadmap
How did I come up with this?

I want to learn English faster, so I created this. At first, I used Notion to store vocabulary as a database, and grammar, writing tips, speaking samples as pages. I coded the pronounce crawling feature from Cambridge, then used Notion's database API to push the data to my vocab database.
I also coded the antonym/synonym crawling from [Thesaurus.com](https://www.thesaurus.com/), and beautified the result in the console using `rich`.

Soon, I realized Notion is too laggy for me when the database is large, not for the long run. So I switched to Anki, taking the advantage of Space repetition method. I crawl vocab pronounce (reduce crawling time using `asyncio`), then import it to Anki, with [my custom template](/anki_template.html). 

But since I watched [this](https://www.youtube.com/watch?v=--Hu2w0s72Y), I decided to take a different approach...

Now: I am working on the CLI version. Because opening a text file with 1k lines seems ineffective in VSCode...


## Features
- Crawl vocabs pronunciation

## Structure
- [`cambridge.py`](/cambridge.py): Crawl pronunciation of vocabulary from Crambridge Dictionary
- [`el.py`](/el.py) [***WIP***]: CLI tool to learn English
- [`logger.py`](/logger.py): Log information to `runtime.log`
- [`ludwigy.py`](/ludwigy.py) [***WIP***]: act like [Ludwig.guru](https://app.ludwig.guru/), no limitation
- [`main.py`](/main.py): Crawl the pronunciation of vocab and write to a file to import to Anki
- [`quizlet.py`](/quizlet.py): Small script to format the exported result from Quizlet
- [`rich_format.py`](/rich_format.py): Format text for rich library
- [`utils.py`](/utils.py): Timing code, Read and format vocabs from raw file, Clear file, Find duplicate vocabs
    - The reason to format: I used Onetab, and when saving Cambridge page to Onetab, it has the following format: `<VOCAB> | English meaning - Cambridge Dictionary`, so I need to remove the part after `|`
- [`deprecated/`](/deprecated/): Folder contains some deprecated/old scripts:
    - `notion`: Interact with Notion database using API, not sure if the code still works
    - `thesaurus.py`: Crawl synonyms of vocab on thesaurus.com

## How to use

Install dependencies:
- Python library 
```py
pip install requests dotenv beautifulsoup4 aiofiles tqdm rich click
```
- fzf

Create a `.env` file with the following format:
```
USER_AGENT = <your user agent>
```
You can find your user agent [here](https://www.google.com/search?q=find+user+agent)
- Write all your vocabulary to `vocabs.txt` (create if you don't have it).
- `main.py` will crawl the pronunciation of the word and then write it to `result.txt`
- If you want to crawl vocab definition, take a look at [mhwgoo/cambridge](https://github.com/mhwgoo/cambridge). I can't implement the crawl definition feature 🥲.

## TODO
- [x] Complete Roadmap story
- [ ] Create a chatbot for writing skills, checking grammar...
    - [ ] Mistral? find model specific for english learning, or finetune it...
- [ ] Convert to database? does it faster?
- [ ] Rewrite it to CLI using Click + fzf
    - [ ] convert it to a module?
    - [ ] implement trie with auto suggestion instead of fzf?
        - [ ]  python + go lib: https://github.com/charmbracelet
        - [ ]  or interactive python CLI? REPL?
    - [ ] n random vocabs + LLM to generate sentence/paragraph for given vocab
        - [ ] Call Gemini API?
- [ ] restructure folder, and files

## Some good resources 🔥
- [IELTS Online Tests](https://ieltsonlinetests.com/ielts-exam-library#academic-test)
- [Dictionary Look Up](https://github.com/ngntrgduc/Dictionary-Look-Up): Browser extension for quickly look up for vocabs.
- [The Best (and Worst) IELTS Websites - TED IELTS](https://ted-ielts.com/ielts-website-review/)

For Vietnamese:
- https://www.tuhocielts.online/
- https://study4.com/

### Happy learning 🐧