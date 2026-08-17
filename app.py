from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/quote")
def quote() -> dict[str, int | str]:
    return {"currency": "USD", "amount": 100}
