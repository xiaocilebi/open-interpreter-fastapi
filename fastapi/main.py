from typing import Union
import base64

import interpreter

from fastapi import FastAPI

from .logger import logger


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
def oi() -> dict[str, str]:
    message_raw: str = "ハローワールドを書いて"  # just for testing
    message: bytes = base64.b64encode(message_raw.encode("utf-8")).decode(
        "utf-8"
    )  # just for testing
    decoded_message: str = base64.b64decode(message).decode("utf-8")
    logger.info("message: " + decoded_message)
    output: list[str] = []
    chunk: dict
    for chunk in interpreter.chat(decoded_message, display=False, stream=True):
        logger.info("chunk: {} ({})".format(chunk, chunk.keys() ))
        if "message" in chunk:
            output.append(chunk["message"])
    return {"message": "".join(output)}
