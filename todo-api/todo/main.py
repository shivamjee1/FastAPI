from fastapi import FastAPI

app = FastAPI()


@app.get("/todo")
def todo():
    return {"massage": "this is todo app"}