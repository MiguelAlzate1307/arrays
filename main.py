from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/arr")
async def arr(req: Request):
    body = await req.json()
    return body

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
