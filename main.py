from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"result": a + b}