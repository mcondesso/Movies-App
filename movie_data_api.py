import os
import requests


OMDB_API_URL = "http://www.omdbapi.com/"


def get_movie_data(title):
    """Fetch movie data from the OMDb API."""
    API_KEY = os.getenv("API_KEY")

    params = {"t": title, "apikey": API_KEY}
    try:
        response = requests.get(OMDB_API_URL, params=params)
        response.raise_for_status()
        json_response = response.json()
    except requests.exceptions.RequestException as error:
        return {"error": f"Request failed: {error}"}

    if json_response.get("Response") == "False":
        return {"error": json_response.get("Error", "Unknown error")}
    return {
        "title": json_response.get("Title", "N/A"),
        "year": json_response.get("Year", "N/A"),
        "rating": json_response.get("imdbRating", "N/A"),
        "poster_image_url": json_response.get("Poster", None),
    }
