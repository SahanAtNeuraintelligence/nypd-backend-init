from beanie import Document
from pydantic import BaseModel


class UserBase(BaseModel):
    ...


class User(Document):
    email: str
    username: str
    isAdmin: bool = False
    password: str

    # @staticmethod
    # async def get_all(limit: int = 12, skip: int = 0):
    #     return await User.find_all(limit=limit, skip=skip).to_list()

    @staticmethod
    async def create_user(email: str, password: str, username: str):
        return await User(email=email, password=password, username=username).insert()

    @staticmethod
    async def is_admin(_id):
        user = await User.get(document_id=_id)
        if not user:
            return False
        else:
            return user.isAdmin
