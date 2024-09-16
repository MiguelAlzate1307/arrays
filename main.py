from fastapi import FastAPI
from fastapi.openapi.models import RequestBody

app = FastAPI()

@app.post("/arr")
def arr(list: RequestBody):
    print(list)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
