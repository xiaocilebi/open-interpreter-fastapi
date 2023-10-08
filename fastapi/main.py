from typing import Union

from fastapi import FastAPI

import interpreter

interpreter.model = "gpt-3.5-turbo"
interpreter.auto_run = True
interpreter.system_message += """
Run shell commands with -y so the user doesn't have to confirm them.
"""


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/oi/")
def oi() -> str:
    message = "日本の首都はどこですか？"
    text = ""
    for chunk in interpreter.chat(message, display=False, stream=True):
        text += str(chunk)
    return {"message": text}
