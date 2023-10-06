from pydantic import BaseModel, EmailStr, constr


class Message(BaseModel):
    to: EmailStr
    subject: constr(min_length=1)
    content: constr(min_length=1)
