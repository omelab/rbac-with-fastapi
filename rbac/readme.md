# Write Modularized RBAC configuration

##  Directory Structure
 
project/
├── app/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── auth_router.py
│   │   ├── auth_service.py
│   │   ├── auth_models.py
│   │   └── auth_schemas.py
│   ├── user/
│   │   ├── __init__.py
│   │   ├── user_router.py
│   │   ├── user_service.py
│   │   ├── user_models.py
│   │   └── user_schemas.py
│   ├── admin/
│   │   ├── __init__.py
│   │   ├── admin_router.py
│   │   ├── admin_service.py
│   │   ├── admin_models.py
│   │   └── admin_schemas.py
│   ├── main.py
│   ├── database.py
│   └── middleware/
│       ├── __init__.py
│       └── rbac.py
└── requirements.txt

##  environment variable configure

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

Create a file ```main.py``` with:

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

Run the server with:

```bash
uvicorn main:app --reload
```


4. Install Database dependencies

Install SQLAlchemy

```bash
pip install sqlalchemy[asyncio] asyncpg
```



There is many ways to install database dependencies, you can flow [this](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=alembic#alembic-note) tutorials for that or you can look this video [tutorials](https://www.youtube.com/watch?v=nC9ob8xM3AM) or [this video](https://www.youtube.com/watch?v=2g1ZjA6zHRo) or [this](https://www.youtube.com/watch?v=UbSONbZ8t4g&list=PLhH3UpV2flrwfJ2aSwn8MkCKz9VzO-1P4) also you can flow this [guide](https://www.educative.io/answers/how-to-use-postgresql-database-in-fastapi)





## requirements
you can create requirements.txt file manually and list the dependencies,

```makefile 
annotated-types==0.6.0
anyio==4.2.0
click==8.1.7
fastapi==0.109.2
h11==0.14.0
idna==3.6
pydantic==2.6.1
pydantic_core==2.16.2
sniffio==1.3.0
starlette==0.36.3
typing_extensions==4.9.0
uvicorn==0.27.0.post1
```

 or you can use the following command to generate it automatically based on the currently installed packages in your environment:

 ```bash
 pip freeze > requirements.txt
 ```



## Modular FastAPI Application:


https://www.youtube.com/watch?v=d_ugoWsvGLI
https://www.youtube.com/watch?v=Lj7ivxUvSog
https://www.youtube.com/watch?v=UbSONbZ8t4g&list=PLhH3UpV2flrwfJ2aSwn8MkCKz9VzO-1P4
https://www.youtube.com/watch?v=nC9ob8xM3AM
https://www.youtube.com/watch?v=2g1ZjA6zHRo
https://www.educative.io/answers/how-to-use-postgresql-database-in-fastapi
