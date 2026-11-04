import requests
import argparse
from dataclasses import dataclass
from typing import Optional, List, Any
import json
from magazine.Brewery import Brewery

def returnstr(name, surname):
    return "Cześć " + name + " " + surname + "!"

def multiply(num1, num2):
    return num1 * num2

def checkifeven(num):
    return num % 2 == 0

def comparethree(one, two, three):
    return one + two >= three

def isinlist(list, num):
    return num in list

def merge(lista1: list, lista2: list) -> list:
    return [x ** 3 for x in set(lista1 + lista2)]

def fetch_breweries(limit: int = 20) -> List[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        "per_page": limit,
        "page": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # rzuci wyjątek dla błędów HTTP
        data = response.json()
        return [Brewery.from_dict(item) for item in data]
    except requests.RequestException as e:
        print(f"Błąd podczas łączenia z API: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Błąd podczas parsowania odpowiedzi JSON: {e}")
        return []

def main():
    print("Pobieranie 20 pierwszych browarów z Open Brewery DB...\n")
    breweries = fetch_breweries(limit=20)

    if not breweries:
        print("Nie udało się pobrać danych. Sprawdź połączenie z internetem.")
        return

    print(f"Pobrano {len(breweries)} browarów:\n")
    print("=" * 60)

    for i, brewery in enumerate(breweries, start=1):
        print(f"\n[{i}] {brewery}")
        print("-" * 60)

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


def fetch_breweriesalt(limit: int = 20,
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


def mainalt():
    args = parse_arguments()

    if args.city:
        string = f"Pobieranie browarów dla miasta: {args.city}"
        print(string + "(limit: {args.limit})...\n")
    else:
        string = f"Pobieranie {args.limit} pierwszych"
        print(string + "browarów (bez filtra miasta)...\n")

    breweries = fetch_breweriesalt(limit=args.limit, city=args.city)

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