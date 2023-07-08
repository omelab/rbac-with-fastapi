## FastAPI

in this section we will discuse about FastAPI and learn Python Basics
we will create some of projects using FastAPI like

- CRM
- HRM
- POS
- ECOMMERCE

### Installation and setup

first we need to check my installation python version and confirm that

```bash
python3 --version

#output Python 3.11.3
```

#### Setup virtual environment

in this section we will create a virtual environment

#### Install pip first

The PIP can be downloaded and installed using the command line by going through the following steps:
if you are using windows please flow [this instructions](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)

To use Homebrew to install PIP on a Mac:

1. Open the Terminal app via the Launchpad menu.
2. In the Terminal window, type `brew install python` and press Enter
3. Homebrew will install the latest version of Python (including PIP). Allow time for it to complete.
4. To finalize your PIP installation, type `brew unlink python && brew link python` and press Enter.

To check your PIP version on a Mac: `pip --version` or `python3 -m pip --version`

To upgrade your PIP version on a Mac using the following command: `python3 -m pip install --upgrade pip`

#### install virtualenv using pip

```bash
sudo pip install virtualenv
```

#### create a virtual environment

```bash
virtualenv venv
```

> you can use any name insted of **venv**

#### You can also use a Python interpreter of your choice

```bash
python3 -m venv /path/to/new/virtual/environment
```

#### Active your virtual environment:

```bash
source /path/to/new/virtual/environment/bin/activate
```

#### Install FastAPI

```bash
pip install fastapi
```

You will also need an ASGI server, for production such as [Uvicorn](https://www.uvicorn.org/)

```bash
pip install uvicorn
```

### Create Simple Crud

in this section we will create a simple crud script, we need to create a file main.py in root directory

```python

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```

### Run it

```bash
uvicorn main:app --reload
```

### Check it

Open your browser at [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery)

You will see the JSON response as:

```json
{ "item_id": 5, "q": "somequery" }
```

You already created an API that:

1. Receives HTTP requests in the paths `/` and `/items/{item_id}`.
2. Both paths take `GET` operations (also known as HTTP methods).
3. The path `/items/{item_id}` has a path parameter `item_id` that should be an `int`.
4. The path `/items/{item_id}` has an optional `str` query parameter `q`.

### Interactive API docs

Now go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui))

### Alternative API docs

And now, go to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

You will see the alternative automatic documentation (provided by [ReDoc](https://github.com/Redocly/redoc)):

### Example upgrade

Now modify the file main.py to receive a body from a PUT request.

Declare the body using standard Python types, thanks to Pydantic.

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

The server should reload automatically (because you added --reload to the uvicorn command above).
