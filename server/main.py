from fastapi import FastAPI
from pathlib import Path
import json

CURRENT_PATH = Path(__file__).parent.resolve()
db = {
    token["id"]: token
    for token in json.load(open(Path(CURRENT_PATH, "database.json")))["tokens"]
}

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "See the metadata for a token by going to /tokens/{token_id}"}


@app.get("/tokens/{token_id}")
async def get_token(token_id: int):
    return db[token_id]
