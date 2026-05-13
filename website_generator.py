HTML_TEMPLATE_FILEPATH = "_static/index_template.html"
HTML_OUTPUT_FILEPATH = "_static/index.html"


def serialize_movie(movie_title, movie_data):
    """Serialize a movie into an HTML list item."""
    if movie_data["poster_url"]:
        poster_html = (
            f'<img class="movie-poster" src="{movie_data["poster_url"]}" alt="..."/>'
        )
    else:
        poster_html = '<div class="no-poster">No poster available</div>'
    return f"""
    <li>
        <div class="movie">
            {poster_html}
            <div class="movie-title">{movie_title}</div>
            <div class="movie-year">{movie_data["year"]}</div>
        </div>
    </li>
    """


def generate_website(movies):
    """Generate a simple HTML page with movie posters and ratings."""
    with open(HTML_TEMPLATE_FILEPATH, "r", encoding="utf-8") as handle:
        html_template = handle.read()

    if movies:
        serialized_movies = "".join(
            [serialize_movie(title, data) for title, data in movies.items()]
        )
    else:
        serialized_movies = "<p>No movies in the database yet</p>"

    html_content = html_template.replace("__TEMPLATE_TITLE__", "My Movie Collection")
    html_content = html_content.replace("__TEMPLATE_MOVIE_GRID__", serialized_movies)

    with open(HTML_OUTPUT_FILEPATH, "w", encoding="utf-8") as handle:
        handle.write(html_content)

    print("Website was generated successfully.")
