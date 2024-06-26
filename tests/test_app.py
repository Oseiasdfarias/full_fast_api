from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get("/")  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    assert response.json() == {"message": "Olá Mundo!"}  # Assert


def test_create_user(client):

    response = client.post(  # UserScrema
        "/users/",
        json={
            "username": "osieas",
            "email": "user@example.com",
            "password": "string"
        }
    )

    # Validar UserPublic
    assert response.status_code == HTTPStatus.CREATED  # Assert (Afirmação)
    assert response.json() == {
        "username": "osieas",
        "email": "user@example.com",
        "id": 1
    }
