from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_api.schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.get("/olamundo", status_code=HTTPStatus.OK, response_class=HTMLResponse)
def ola_mundo():
    return """
        <html>
            <head>
                <title> FastAPI </title>
            </head>
            <body>
                <h1> Olá, Mundo! <h1>
            </body>
        </html> """
