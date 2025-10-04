from fastapi import FastAPI

app = FastAPI()

def read_root():
    return('Hello, world!')

def red_item(item_id: int, q: str | None = None):
    return{'item_id': item_id, 'q': q}