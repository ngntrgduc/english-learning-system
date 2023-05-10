# English-learning-system
My English learning system, with Notion.

## pronouce.py
Contain functions to crawl vocabulary from database, find missing pronounce and update pronounce

## main.py
- Read vocabulary from file, and push to Notion database
- Crawl vocabulary database on Notion, find missing pronounce and update

## notion.py
Contain create, read and update database functions on Notion using Notion API

## thesaurus.py
Crawl synonyms from Thesaurus.com

## split_vocab.py
Split vocabulary from words.txt 

## flashcard.py
(WIP) Learn vocabulary using flashcard-like in CLI

## utils
- tictoc.py: Timing code
- vocabs.py: Read and format vocabulary from raw file

# TODO
- [ ] CLI arguments

## How to use
- Create `.env` file with the following format:
```
USER_AGENT = <your user agent>
NOTION_TOKEN = <your Notion token>
VOCAB_DATABASE_ID = <your vocabulary database id>
```
find user agent [here](https://www.google.com/search?q=find+user+agent)