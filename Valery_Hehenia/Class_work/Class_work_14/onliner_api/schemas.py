from pydentic import BaseModel

class ProductSchema(BaseModel):
    id: int
    name: str
    key: str
    description: str | None
    amount: float

class CurrencySchema(BaseModel):
    USD: float
    RUB: float
    EUR: float


