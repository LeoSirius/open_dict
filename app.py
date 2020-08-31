from fastapi import FastAPI

app = FastAPI()


@app.get("/api/")
def read_root(word):
    print('type word = {}'.format(type(word)))
    print('word = {}'.format(word))
    return {"Hello": "World"}