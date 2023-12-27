from pydantic import BaseModel, Field


class GetUserListResponseSchema(BaseModel):
    email: str = Field(..., description="Email")
    username: str = Field(..., description="Username")


class CreateUserRequestSchema(BaseModel):
    email: str = Field(..., description="Email")
    password: str = Field(..., description="Password1")
    username: str = Field(..., description="Username")


class CreateUserResponseSchema(BaseModel):
    email: str = Field(..., description="Email")
    username: str = Field(..., description="Username")
