import argparse
import json
import requests
from dataclasses import dataclass
from typing import Optional, List
from magazine.Brewery import Brewery

def parse_arguments() -> argparse.Namespace:
    """Parsuje argumenty wiersza poleceń."""
    parser = argparse.ArgumentParser(
        description="Pobiera browary z Open Brewery DB.",
        epilog="Przykład: python main.py --city=Berlin"
    )
    string = "Nazwa miasta, według którego mają"
    parser.add_argument(
        "--city",
        type=str,
        default=None,
        help=string + " być filtrowane browary (np. Berlin)."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Liczba browarów do pobrania (domyślnie 20)."
    )
    return parser.parse_args()


def fetch_breweries(limit: int = 20,
                    city: Optional[str] = None) -> List[Brewery]:
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
        string = f"Pobieranie browarów dla miasta: {args.city}"
        print(string + "(limit: {args.limit})...\n")
    else:
        string = f"Pobieranie {args.limit} pierwszych"
        print(string + "browarów (bez filtra miasta)...\n")

    breweries = fetch_breweries(limit=args.limit, city=args.city)

    if not breweries:
        if args.city:
            print(f"Nie znaleziono browarów dla miasta: {args.city}.")
        else:
            string = "Nie udało się pobrać danych."
            print(string + "Sprawdź połączenie z internetem.")
        return

    print(f"Pobrano {len(breweries)} browarów:\n")
    print("=" * 60)

    for i, brewery in enumerate(breweries, start=1):
        print(f"\n[{i}] {brewery}")
        print("-" * 60)