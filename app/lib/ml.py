import ollama
import os

def g(model, inputText):
    response = ollama.generate(model, inputText)
    return response

def text(inputText, model=""):
    if model == "":
        model = os.environ["OLLAMA_MODEL"]
    r = g(model=model, inputText=inputText)
    return r["response"]

if __name__ == "__main__":
    import sys
    i = sys.argv[1]
    r = text(i)
    print("{}".format(r))