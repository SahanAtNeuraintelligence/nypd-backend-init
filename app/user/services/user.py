from typing import List, Optional

from app.user.models.user import User


class UserService:
    def __init__(self):
        ...

    @staticmethod
    async def get_user_list(
        limit: int = 12,
        skip: Optional[int] = None,
    ) -> List[User]:
        return await User.all(limit=limit, skip=skip).to_list()

    @staticmethod
    async def create_user(email: str, password: str, username: str) -> None:
        return await User.create_user(email=email, password=password, username=username)

    @staticmethod
    async def is_admin(_id: str) -> bool:
        return await User.is_admin(_id)
