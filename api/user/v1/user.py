from typing import List, Optional

from fastapi import APIRouter

from app.user.schemas import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserListResponseSchema,
)
from app.user.services.user import UserService

user_router = APIRouter()


@user_router.post(
    "",
    response_model=CreateUserResponseSchema,
    # responses={"404": {"model": ExceptionResponseSchema}},
)
async def create_user_route(request: CreateUserRequestSchema):
    email: str = request.email
    password: str = request.password
    username: str = request.username
    return await UserService().create_user(
        email=email, password=password, username=username
    )


@user_router.get(
    "",
    response_model=List[GetUserListResponseSchema],
    response_model_exclude={"id"},
    # responses={"400": {"model": ExceptionResponseSchema}},
    # dependencies=[Depends(PermissionDependency([IsAdmin]))],
)
async def get_user_list(
    limit: int = 12,
    skip: Optional[int] = None,
):
    return await UserService().get_user_list(limit=limit, skip=skip)
