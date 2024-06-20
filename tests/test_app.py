from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (Organização do teste)

    response = client.get("/")  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    assert response.json() == {"message": "Olá Mundo!"}  # Assert


def test_ola_mundo_deve_retornar_ok_e_html():
    client = TestClient(app)  # Arrange (Organização do teste)

    response = client.get("/olamundo")  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    print(response.text)
    assert response.text == """
        <html>
            <head>
                <title> FastAPI </title>
            </head>
            <body>
                <h1> Olá, Mundo! <h1>
            </body>
        </html> """   # Assert
