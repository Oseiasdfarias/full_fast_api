from http import HTTPStatus

from fast_api.schemas import UserPublic


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirmação)
    assert response.json() == {"message": "Olá Mundo!"}  # Assert


def test_create_user_username_existing(client, user):
    response = client.post(  # UserScrema
        "/users/",
        json={
            "username": user.username,
            "email": "user@example.com",
            "password": "string",
        },
    )

    # Validar UserPublic
    assert response.status_code == HTTPStatus.BAD_REQUEST  # Assert (Afirmação)
    assert response.json() == {"detail": "Usermane already exists."}


def test_create_user_email_existing(client, user):
    response = client.post(  # UserScrema
        "/users/",
        json={
            "username": "teste",
            "email": user.email,
            "password": "string",
        },
    )

    # Validar UserPublic
    assert response.status_code == HTTPStatus.BAD_REQUEST  # Assert (Afirmação)
    assert response.json() == {"detail": "Email already exists."}


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
    assert response.json() == {"users": []}


def test_read_users_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get("/users")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": [user_schema]}


def test_read_user(client):
    response = client.get("/users/1")
    print(response.json())
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found."}


def test_read_user_with_user(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_schema


def test_update_user(client, user, token):
    response = client.put(
        f"/users/{user.id}",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "password": "123",
            "username": "test_username",
            "email": "user@example.com",
            "id": user.id,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "test_username",
        "email": "user@example.com",
        "id": user.id,
    }


def test_update_user_not_found(client, token):
    response = client.put(
        "/users/2",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "password": "123",
            "username": "test_username",
            "email": "user@example.com",
            "id": 2,
        },
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Not enough permission."}


def test_delete_user(client, user, token):
    response = client.delete(
        f"/users/{user.id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted!"}


def test_delete_user_not_oermission(client, user, token):
    response = client.delete(
        f"/users/{2}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'Not enough permission.'}


def test_delete_user_not_found(client, user):
    response = client.delete("/users/2")
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}


def test_get_token(client, user):
    response = client.post(
        "/token",
        data={"username": user.email, "password": user.clean_password},
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token["token_type"] == "bearer"
    assert "access_token" in token


def test_get_token_incorret_email(client, user):
    response = client.post(
        "/token",
        data={"username": "test.test", "password": user.clean_password},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Incorrect email or password."}


def test_get_token_incorret_password(client, user):
    response = client.post(
        "/token",
        data={"username": user.email, "password": "1234"},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Incorrect email or password."}
