import json

DATABASE_FILE = "movies.json"


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    with open(DATABASE_FILE, "r") as movies_db:
        movies = json.load(movies_db)

    return movies


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open(DATABASE_FILE, "w") as movies_db:
        json.dump(movies, movies_db, indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, adds the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open(DATABASE_FILE, "r") as movies_db:
        movies = json.load(movies_db)

    movies[title] = {"rating": rating, "year": year}

    with open(DATABASE_FILE, "w") as movies_db:
        json.dump(movies, movies_db, indent=4)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open(DATABASE_FILE, "r") as movies_db:
        movies = json.load(movies_db)

    if title in movies:
        del movies[title]

    with open(DATABASE_FILE, "w") as movies_db:
        json.dump(movies, movies_db, indent=4)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    with open(DATABASE_FILE, "r") as movies_db:
        movies = json.load(movies_db)

    if title in movies:
        movies[title]["rating"] = rating

    with open(DATABASE_FILE, "w") as movies_db:
        json.dump(movies, movies_db, indent=4)
