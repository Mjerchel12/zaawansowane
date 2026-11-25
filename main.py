from pathlib import Path
import csv

from fastapi import FastAPI

app = FastAPI(title="MovieLens API")

DATA_DIR = Path(__file__).parent / "data"


# ----------------------------
# Modele danych
# ----------------------------
class Movie:
    def __init__(self, movie_id: str, title: str, genres: str):
        self.movieId = int(movie_id)
        self.title = title
        self.genres = genres.split("|")


class Link:
    def __init__(self, movie_id: str, imdb_id: str, tmdb_id: str):
        self.movieId = int(movie_id)
        self.imdbId = int(imdb_id) if imdb_id else None
        self.tmdbId = int(tmdb_id) if tmdb_id else None


class Rating:
    def __init__(self, user_id: str, movie_id: str, rating: str, timestamp: str):
        self.userId = int(user_id)
        self.movieId = int(movie_id)
        self.rating = float(rating)
        self.timestamp = int(timestamp)


class Tag:
    def __init__(self, user_id: str, movie_id: str, tag: str, timestamp: str):
        self.userId = int(user_id)
        self.movieId = int(movie_id)
        self.tag = tag
        self.timestamp = int(timestamp)


# ----------------------------
# Ładowanie danych z plików
# ----------------------------
def load_movies() -> list[Movie]:
    movies: list[Movie] = []
    with open(DATA_DIR / "movies.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            movies.append(Movie(row["movieId"], row["title"], row["genres"]))
    return movies


def load_links() -> list[Link]:
    links: list[Link] = []
    with open(DATA_DIR / "links.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            links.append(Link(row["movieId"], row["imdbId"], row["tmdbId"]))
    return links


def load_ratings() -> list[Rating]:
    ratings: list[Rating] = []
    with open(DATA_DIR / "ratings.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ratings.append(
                Rating(row["userId"], row["movieId"], row["rating"], row["timestamp"])
            )
    return ratings


def load_tags() -> list[Tag]:
    tags: list[Tag] = []
    with open(DATA_DIR / "tags.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            tags.append(
                Tag(row["userId"], row["movieId"], row["tag"], row["timestamp"])
            )
    return tags


# ----------------------------
# Endpointy
# ----------------------------
@app.get("/")
def hello_world():
    """Zadanie 1 – hello world."""
    return {"hello": "world"}


@app.get("/movies")
def get_movies():
    """Zadanie 2 – lista filmów."""
    return [movie.__dict__ for movie in load_movies()]


@app.get("/links")
def get_links():
    """Zadanie 4 – linki (IMDb, TMDb)."""
    return [link.__dict__ for link in load_links()]


@app.get("/ratings")
def get_ratings():
    """Zadanie 4 – oceny filmów."""
    return [rating.__dict__ for rating in load_ratings()]


@app.get("/tags")
def get_tags():
    """Zadanie 4 – tagi przypisane do filmów."""
    return [tag.__dict__ for tag in load_tags()]