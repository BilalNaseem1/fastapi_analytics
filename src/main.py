from typing import Union
from fastapi import FastAPI

from api.events import events_router

app = FastAPI()
app.include_router(events_router, prefix='/api/events', tags=['events'])

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



# health check
@app.get("/healthz")
def health_check():
    return {"status": "ok"}