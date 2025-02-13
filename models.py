from pydantic import BaseModel, Field, EmailStr

class UserLogin(BaseModel):
    """
    Login Model:
    - username: Huruf, angka, dan underscore
    - password: Huruf, angka, spasi, dash, dan underscore
    """
    username: str = Field(min_length=8, max_length=64, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(min_length=8, max_length=255, pattern=r"^[a-zA-Z0-9\s_-]+$")

class UserRegister(BaseModel):
    """
    Register Model:
    - fullname: Huruf, angka, dan spasi
    - username: Huruf, angka, dan underscore
    - password: Huruf, angka, spasi, dash, dan underscore
    - email: Format email valid
    - phone: Opsional
    """
    fullname: str = Field(min_length=3, max_length=255, pattern=r"^[a-zA-Z0-9\s]+$")
    username: str = Field(min_length=8, max_length=64, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(min_length=8, max_length=255, pattern=r"^[a-zA-Z0-9\s_-]+$")
    email: EmailStr
    phone: str | None = None
