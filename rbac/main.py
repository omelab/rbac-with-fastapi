from typing import Union
from fastapi import FastAPI

app = FastAPI(
    title = "RBAC API",
    description = "This is simple RBAC API for best practice development",
    docs_url = "/",
)

@app.get("/notes")
async def get_all_notes():
    return {"message": "Hello World"}

@app.post("/notes")
async def create_notes():
    pass

@app.get("/notes/{note_id}")
async def get_note_by_id(note_id: int, q: Union[str, None] = None):
    return {"item_id": note_id, "q": q}

@app.put("/notes/{note_id}")
async def update_note():
    pass

@app.delete("/notes/{note_id}")
async def delete_note():
    pass
