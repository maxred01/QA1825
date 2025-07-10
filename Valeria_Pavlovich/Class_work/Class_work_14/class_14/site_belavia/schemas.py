from pydantic import BaseModel
from typing import Optional, List


class AirportInfo(BaseModel):
    cityId: int
    airportCode: str
    airportName: str


class Segment(BaseModel):
    departure: AirportInfo
    arrival: AirportInfo
    departureDate: str
    flightNumber: str
    serviceClass: str


class PriceDetails(BaseModel):
    amount: float
    currency: str


class Itinerary(BaseModel):
    segments: List[Segment]
    price: PriceDetails
