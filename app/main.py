import os
from lib import ml
from typing import Annotated
from fastapi import FastAPI, Response, Form

app = FastAPI()


@app.get("/")
def read_root(response: Response):
    # This is basically a health-check
    response.headers["Cache-Control"] = "no-cache, no-store"
    healthJSON = {"online": True}
    return healthJSON

@app.post("/")
def root(response: Response, q: Annotated[str, Form()], model: Annotated[str, Form()] = None):
    response.headers["Cache-Control"] = "no-cache, no-store"
    responseDict = {}
    prompt = "SYSTEM: {}\nUSER: '{}'".format(os.environ["SYSTEM_PROMPT"], q)
    print("Prompt: {}".format(prompt))
    if model != None:
        answer = ml.text(prompt, model=model)
    else:
        answer = ml.text(prompt)
    # If you're using one of the deepseek models (or any "thinking" model)
    # then you'll want to trim out all of that text before feeding it back.
    if answer.find("</think>") == -1:
        print("</think> doesn't seem to be in the ml output")
    else:
        trimLine = answer.find("</think>") + len("</think>")
        answer = str(answer[trimLine:]).strip()
    print("Answer: {}".format(answer))
    responseDict["success"] = True
    responseDict["answer"] = answer
    return responseDict