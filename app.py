from fastapi import FastAPI
from word_scraper import word_scraper

app = FastAPI()

@app.get("/{word}/")
def read_root(word: str):
    res = {
        'name': word,
        'meanings': word_scraper(word)
    }
    return res
