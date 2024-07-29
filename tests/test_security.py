import pytest
from jwt import DecodeError, decode

from fast_api.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data = {"sub": "test@test.com"}
    token = create_access_token(data)

    result = decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    assert result["sub"] == data["sub"]
    assert result["exp"]


def test_jwt_invalid_token(client):

    with pytest.raises(DecodeError, match="Not enough segments"):
        client.delete(
            "/users/1", headers={"Authorization": "Bearer token-invalido"}
        )
