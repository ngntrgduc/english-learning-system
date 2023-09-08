import logging

logging.basicConfig(level=logging.INFO, filename='runtime.log', filemode='a', 
                    format='%(asctime)s | %(levelname)s - %(message)s',
                    datefmt='%D - %T')

def log(message: str):
    logging.info(message)

def error(message: str):
    logging.error(message)