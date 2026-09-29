from fastapi import FastAPI

app = FastAPI()


@app.get("/sumar")
def sumar(a: int, b: int):
    return {
        "resultado": a + b
    }