

## Help tools

- [API Framework](https://fastapi.tiangolo.com/)
- [Learn](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Typer](https://typer.tiangolo.com/) For CLI Application Development
- [Starlette](https://www.starlette.io/) is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
- [Pydantic](https://docs.pydantic.dev/latest/)  is the most widely used data validation library for Python.


## Tutorials guide

- [Fast API official Tutorials](https://fastapi.tiangolo.com/tutorial/)




## Installation Guide

1. first you can install python from [here](https://www.python.org/) on your machine
2. you need virtual environment setup from [here](https://docs.python.org/3/library/venv.html) flowing step by step

```bash
# create environment variables
python3 -m venv /path/to/new/virtual/environment

# active environment
source /path/to/new/virtual/invironment/bin/activate
```

3. Install FastAPI

```bash
pip install fastapi

```

You will also need an ASGI server, for production such as [Uvicorn](https://www.uvicorn.org/) or [Hypercorn](https://github.com/pgjones/hypercorn).

```bash
pip install "uvicorn[standard]"
```

if you have install uvicorn you can check version like:

```bash
uvicorn --version
# unning uvicorn 0.25.0 with CPython 3.11.6 on Darwin
```


write your first python file called `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"message": "About"}


@app.get("/blog/{id}")
def about(id):
    return {"message": id}

@app.get("/blog/{id}/comments")
def about(id:int):
    return {"message": 'comments for ' + str(id)}
```
write the flowing command on your terminnal  to run your project 

```bash
uvicorn main:app --reload

```
