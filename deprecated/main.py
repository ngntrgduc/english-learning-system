"""Crawl pronounce of vocab and write to a file to import to Anki"""

import time
import random
import asyncio

import aiofiles
from tqdm import tqdm

import deprecated.cambridge as cambridge
from utils import read, clear_file
import logger

async def main():
    file_name = 'vocabs'
    tic = time.time()
    vocabs = read(f'{file_name}.txt')
    async with aiofiles.open(f'{file_name}.result.txt', 'w', encoding='utf-8') as f:
        for vocab in tqdm(vocabs, desc='Crawl & create', unit='word'):
            await asyncio.sleep(random.uniform(0, 0.5) + 0.5)
            pronounce = await cambridge.crawl(vocab)
            await f.write(f'{vocab},{pronounce}\n')
    
    clear_file(f'{file_name}.txt')

    logger.info(f'Crawled {len(vocabs)} vocabs, took {(time.time()-tic)/60:.3f} mins, sleep 0.5-1s')

asyncio.run(main())
