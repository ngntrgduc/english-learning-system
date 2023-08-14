# English-learning-system
My English learning system ~~for IELTS~~, with Anki (used to use Notion. But I realized that Notion is not for the long run because it's so laggy so I decided to switch to Anki).

## thesaurus.py
Crawl synonyms from Thesaurus.com

## utils
- tictoc.py: Timing code
- vocabs.py: Read and format vocabulary from raw file

## How to use
- Create `.env` file with the following format:
```
USER_AGENT = <your user agent>
```
You can find your user agent [here](https://www.google.com/search?q=find+user+agent)
- Write all your vocabulary to `vocabs.txt`, if you don't have, create one.
- `main.py` will crawl the pronounce of word and then write it to `result.txt`

# TODO
- [ ] Maybe create a chatbot for writing skill...

### Happy learning 🐧