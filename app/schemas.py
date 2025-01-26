from pydantic import BaseModel


class ExampleBase(BaseModel):
    name: str
    description: str


class ExampleCreate(ExampleBase):
    pass


class ExampleResponse(ExampleBase):
    id: int

    class Config:
        orm_mode = True
