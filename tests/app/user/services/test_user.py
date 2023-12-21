import pytest

from app.user.services.user import UserService


@pytest.mark.asyncio
async def test_is_admin():
    assert await UserService().is_admin()
