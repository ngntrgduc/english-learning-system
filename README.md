# English-learning-system
My English learning system ~~for IELTS~~, with Anki. I used to use Notion. 
But I realized that Notion is not for the long run because it's so laggy when 
database is large. So I decided to switch to Anki.

Update: I not use Anki anymore since I watched [this](https://www.youtube.com/watch?v=--Hu2w0s72Y)

## ~~Bugs~~ Features
- No more time-consuming for `Ctrl + C`, `Ctrl + V` vocab pronunciations
- ~~Fast~~ Not too slow... (powered by Asynchronous)

## Structure
- `cambridge`: Crawl pronunciation of vocabulary
- `main`: Crawl pronounce of vocab and write to a file to import to Anki
- `thesaurus.py`: Crawl synonyms from [Thesaurus.com](https://www.thesaurus.com/)
- `utils.py`: Timing code, Read and format vocabs from raw file, Clear file, Find duplicate vocabs
    - Reason to format the file: I used Onetab, and when saving Cambridge page to Onetab, it have the following format: `<VOCAB> | English meaning - Cambridge Dictionary`, so I need to remove the part after `|`
- `logger.py`: Just log to `runtime.log`
- `ludwigy.py` [***WIP***]: act like [Ludwig.guru](https://app.ludwig.guru/), no limitation
- `quizlet.py`: Just a small script to format the export result from Quizlet
- `notion(old)`: Folder contains some old scripts that interact with Notion database, not sure if the code still work

## How to use
- Create `.env` file with the following format:
```
USER_AGENT = <your user agent>
```
You can find your user agent [here](https://www.google.com/search?q=find+user+agent)
- Write all your vocabulary to `vocabs.txt`, if you don't have, create one.
- `main.py` will crawl the pronounce of word and then write it to `result.txt`
    - If you want to crawl vocab definition, take a look at [mhwgoo/cambridge](https://github.com/mhwgoo/cambridge). I can't implement the crawl definition functionality :).

## TODO
- [ ] Maybe create a chatbot for writing skill, checking grammar...
- [ ] CLI?

## Some good resources 🔥
- [IELTS Online Tests](https://ieltsonlinetests.com/ielts-exam-library#academic-test)

### Happy learning 🐧