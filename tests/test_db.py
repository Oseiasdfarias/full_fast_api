from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    user = User(
        username="teste_db",
        email="teste_db@email.com",
        password="test_password",
    )

    session.add(user)
    session.commit()
    resut = session.scalar(
        select(User).where(User.email == "teste_db@email.com")
    )
    assert resut.username == "teste_db"
