from pydantic import BaseModel
from typing import List

class Hotel(BaseModel):
    otahotel_id: str
    master_id: int
    hotel_name: str
    region_id: int
    region_name: str
    country_code: str
    country_name: str
    hotel_kind: str
    hotel_address: str
    slug: str
    region_name_en: str
    country_name_en: str
    is_natdis_critical: bool

class Region(BaseModel):
    id: int
    type: str
    name: str
    country: str
    country_code: str
    currency_code: str
    pretty_slug: str
    slug: str
    is_sales_closed: bool
    name_en: str
    country_en: str
    is_natdis_critical: bool

class BelaviaResponse(BaseModel):
    hotels: List[Hotel]
    regions: List[Region]