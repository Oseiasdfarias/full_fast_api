from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        "/auth/token",
        data={"username": user.email, "password": user.clean_password},
    )

    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert token["token_type"] == "bearer"
    assert "access_token" in token


def test_get_token_incorret_email(client, user):
    response = client.post(
        "/auth/token",
        data={"username": "test.test", "password": user.clean_password},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Incorrect email or password."}


def test_get_token_incorret_password(client, user):
    response = client.post(
        "/auth/token",
        data={"username": user.email, "password": "1234"},
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Incorrect email or password."}
