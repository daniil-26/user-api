from uuid import UUID
from pydantic import BaseModel, Field, constr, EmailStr


class UserBase(BaseModel):
    name: str = Field(..., max_length=64)
    surname: str = Field(..., max_length=64)
    patronymic: str | None = Field(None, max_length=64)
    type: constr(pattern="^(teacher|student|headteacher)$")
    class_name: str | None = Field(None, max_length=8)
    email: EmailStr
    subject: str | None = Field(None, max_length=64)


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserResponse(UserBase):
    id: UUID

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: str | None = Field(None, max_length=64)
    surname: str | None = Field(None, max_length=64)
    patronymic: str | None = Field(None, max_length=64)
    type: constr(pattern="^(teacher|student|headteacher)$") | None = None
    class_name: str | None = Field(None, max_length=8)
    email: EmailStr | None = None
    password: str | None = Field(None, min_length=8)
    subject: str | None = Field(None, max_length=64)

