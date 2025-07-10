from pydantic import BaseModel

class ProductShame(BaseModel):
    id: int
    name: str
    key: str
    description: str |  None
    price: float

class CurrencyShame(BaseModel):
    USD: float
    GBP: float
    JPY: float



