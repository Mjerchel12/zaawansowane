# Zadanie 8
import argparse
import json
import requests
from dataclasses import dataclass
from typing import Optional, List


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
        return (
            f"Browar: {self.name} (ID: {self.id})\n"
            f"  Typ: {self.brewery_type}\n"
            f"  Adres: {self.address_1 or ''} {self.address_2 or ''} {self.address_3 or ''}\n"
            f"  Miasto: {self.city}, {self.state_province} {self.postal_code}, {self.country}\n"
            f"  Współrzędne: ({self.latitude}, {self.longitude})\n"
            f"  Telefon: {self.phone or 'brak'}\n"
            f"  Strona: {self.website_url or 'brak'}"
        )


def parse_arguments() -> argparse.Namespace:
    """Parsuje argumenty wiersza poleceń."""
    parser = argparse.ArgumentParser(
        description="Pobiera browary z Open Brewery DB.",
        epilog="Przykład: python main.py --city=Berlin"
    )
    parser.add_argument(
        "--city",
        type=str,
        default=None,
        help="Nazwa miasta, według którego mają być filtrowane browary (np. Berlin)."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Liczba browarów do pobrania (domyślnie 20)."
    )
    return parser.parse_args()


def fetch_breweries(limit: int = 20, city: Optional[str] = None) -> List[Brewery]:
    """
    Pobiera browary z API Open Brewery DB.
    Jeżeli podano miasto, zawęża wyniki za pomocą parametru by_city.
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        "per_page": limit,
        "page": 1
    }

    if city:
        params["by_city"] = city

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [Brewery.from_dict(item) for item in data]
    except requests.RequestException as e:
        print(f"Błąd podczas łączenia z API: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Błąd podczas parsowania odpowiedzi JSON: {e}")
        return []


def main():
    args = parse_arguments()

    if args.city:
        print(f"Pobieranie browarów dla miasta: {args.city} (limit: {args.limit})...\n")
    else:
        print(f"Pobieranie {args.limit} pierwszych browarów (bez filtra miasta)...\n")

    breweries = fetch_breweries(limit=args.limit, city=args.city)

    if not breweries:
        if args.city:
            print(f"Nie znaleziono browarów dla miasta: {args.city}.")
        else:
            print("Nie udało się pobrać danych. Sprawdź połączenie z internetem.")
        return

    print(f"Pobrano {len(breweries)} browarów:\n")
    print("=" * 60)

    for i, brewery in enumerate(breweries, start=1):
        print(f"\n[{i}] {brewery}")
        print("-" * 60)


if __name__ == "__main__":
    main()