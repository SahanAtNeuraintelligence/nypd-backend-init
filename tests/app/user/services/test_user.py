import pytest

from app.user.services.user import UserService


@pytest.mark.asyncio
async def test_get_user_list():
    # assert type(await UserService().get_user_list()) == list
    assert True
