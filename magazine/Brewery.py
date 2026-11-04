import requests
from dataclasses import dataclass
from typing import Optional, List, Any
import json


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: str
    street: Optional[str]

    @classmethod
    def from_dict(cls, data: dict) -> 'Brewery':
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            brewery_type=data.get('brewery_type', ''),
            address_1=data.get('address_1'),
            address_2=data.get('address_2'),
            address_3=data.get('address_3'),
            city=data.get('city', ''),
            state_province=data.get('state_province', ''),
            postal_code=data.get('postal_code', ''),
            country=data.get('country', ''),
            longitude=data.get('longitude'),
            latitude=data.get('latitude'),
            phone=data.get('phone'),
            website_url=data.get('website_url'),
            state=data.get('state', ''),
            street=data.get('street')
        )

    def __str__(self) -> str:
        stringad = f"  Adres: {self.address_1 or ''}"
        stringad = stringad + f" {self.address_2 or ''}"
        stringad = stringad + f" {self.address_3 or ''}"

        stringcit = f"  Miasto: {self.city},"
        stringcit = stringcit + f" {self.state_province}"
        stringcit = stringcit + f" {self.postal_code}"
        stringcit = stringcit + f", {self.country}"
        return (
            f"Browar: {self.name} (ID: {self.id})\n"
            f"  Typ: {self.brewery_type}\n" +
            stringad+"\n" +
            stringcit+"\n"
            f"  Współrzędne: ({self.latitude}, {self.longitude})\n"
            f"  Telefon: {self.phone or 'brak'}\n"
            f"  Strona: {self.website_url or 'brak'}"
        )

@dataclass
class BreweryAlt:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: str
    street: Optional[str]

    @classmethod
    def from_dict(cls, data: dict) -> 'Brewery':
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            brewery_type=data.get('brewery_type', ''),
            address_1=data.get('address_1'),
            address_2=data.get('address_2'),
            address_3=data.get('address_3'),
            city=data.get('city', ''),
            state_province=data.get('state_province', ''),
            postal_code=data.get('postal_code', ''),
            country=data.get('country', ''),
            longitude=data.get('longitude'),
            latitude=data.get('latitude'),
            phone=data.get('phone'),
            website_url=data.get('website_url'),
            state=data.get('state', ''),
            street=data.get('street')
        )

    def __str__(self) -> str:
        stringad = f"  Adres: {self.address_1 or ''}"
        stringad = stringad + f" {self.address_2 or ''}"
        stringad = stringad + f" {self.address_3 or ''}"

        stringcit = f"  Miasto: {self.city},"
        stringcit = stringcit + f" {self.state_province}"
        stringcit = stringcit + f" {self.postal_code}"
        stringcit = stringcit + f", {self.country}"
        return (
            f"Browar: {self.name} (ID: {self.id})\n"
            f"  Typ: {self.brewery_type}\n" +
            stringad+"\n" +
            stringcit+"\n"
            f"  Współrzędne: ({self.latitude}, {self.longitude})\n"
            f"  Telefon: {self.phone or 'brak'}\n"
            f"  Strona: {self.website_url or 'brak'}"
        )