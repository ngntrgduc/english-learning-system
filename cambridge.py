"""Get pronunciation from Cambridge dictionary"""

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup, SoupStrainer
from logger import exception, info

load_dotenv()

headers = {'User-Agent': os.getenv('USER_AGENT')}

session = requests.Session()

async def crawl(vocab: str) -> str:
    """Crawl and return pronunciations of vocab from Cambridge dictionary"""

    base_url = 'https://dictionary.cambridge.org/dictionary/english/'
    url = base_url + vocab
    response = session.get(url, headers=headers)

    # Check if Cambridge redirect to home page when the vocab not existed
    if response.history:
        if response.history[-1].status_code in range(300, 310):
            if response.url == base_url:
                info(f'"{vocab}" does not exist in the Cambridge dictionary')
                return ''
    
    soup = response.content
    
    page = BeautifulSoup(
        soup, 'lxml',
        parse_only=SoupStrainer(
            'div', attrs={'class': 'pos-header dpos-h'}
        )
    ).findAll(attrs={'class': 'pos-header dpos-h'})

    pronounce_classes = ('uk dpron-i', 'us dpron-i')
    pronounces = []
    pronounce = ''

    for pronounce_class in pronounce_classes:
        try:
            pronounce = page[0].find(attrs={'class': pronounce_class})
            if pronounce:
                pronounce = pronounce.find(attrs={'class': 'pron dpron'}).text
            else:
                pronounce = ''
        except AttributeError:
            # Happen when vocab has different form
            # TODO: still cannot get pronunciations in bellow section
            pronounce = page[1].find(attrs={'class': pronounce_class})
            if pronounce:
                pronounce = pronounce.find(attrs={'class': 'pron dpron'}).text
            else:
                pronounce = ''
        except IndexError:
            info(f'"{vocab}" does not have pronunciation')
            return '"UK: ,  US: "'
        except Exception:
            exception(f'Cannot get pronounce: {vocab}')
        finally:
            pronounces.append(pronounce)
    
    return f'"UK: {pronounces[0]},  US: {pronounces[1]}"'


if __name__ == '__main__':
    import time
    import asyncio
    tic = time.time()
    # for vocab in ['tainted', 'religious', 'no doubt', 'vaporizing', 'hii']:
        # print(vocab, asyncio.run(crawl(vocab)))
    # vocab = 'hii'
    # url = f'https://dictionary.cambridge.org/dictionary/english/{vocab}'
    # res = session.get(url, headers=headers)
    # print(res.history[0].status_code)
    # print(res.status_code)
    print(f'{time.time() - tic}')
