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
            "password": "string",
        },
    )

    # Validar UserPublic
    assert response.status_code == HTTPStatus.CREATED  # Assert (Afirmação)
    assert response.json() == {
        "username": "osieas",
        "email": "user@example.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [{"username": "osieas", "email": "user@example.com", "id": 1}]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "password": "123",
            "username": "test_username",
            "email": "user@example.com",
            "id": 1,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "test_username",
        "email": "user@example.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted!"}
