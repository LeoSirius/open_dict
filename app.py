from typing import List
import time

from fastapi import FastAPI, Query
from pymongo import MongoClient

from word_scraper import word_scraper


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DATABASE_NAME = 'open_dict'


db_client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = db_client[DATABASE_NAME]
words_collection = db['words_collection']


app = FastAPI()
print('in app')


def build_word_document(word_name, meanings):
    return {
        'name': word_name,
        'mtime': int(time.time()),
        'lang_code': 'EN',
        'meanings': meanings,
    }


@app.get('/api/words/{name}/')
async def api_words(name: str):

    word_document = words_collection.find_one({'name': name})
    if not word_document:
        meanings = word_scraper(name)
        word_document = build_word_document(name, meanings)
        words_collection.insert_one(word_document)

    res = {
        'name': name,
        'meanings': word_document['meanings'],
    }
    return res


@app.get('/api/words-batch/')
async def api_words_batch(word: List[str] = Query(None)):
    res_list = []
    for name in word:
        word_document = words_collection.find_one({'name': name})
        if not word_document:
            meanings = word_scraper(name)
            word_document = build_word_document(name, meanings)
            words_collection.insert_one(word_document)
        res = {
            'name': name,
            'meanings': word_document['meanings'],
        }
        res_list.append(res)

    return {
        'word_list': res_list
    }