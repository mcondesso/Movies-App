"""
My Movies Database CLI

This script provides a command-line interface to manage a simple movie database.
Users can list, add, delete, update movies, view statistics, search, and get random
movie recommendations. Ratings are on a scale from 0 to 10.

Commands:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating

The program runs in a loop until interrupted by the user.
"""

import random
import sys
from statistics import median
import movie_storage_sql as movie_storage


def print_menu():
    """Print the menu of available commands."""
    menu_text = (
        "\nMenu:\n"
        "0. Exit\n"
        "1. List movies\n"
        "2. Add movie\n"
        "3. Delete movie\n"
        "4. Update movie\n"
        "5. Stats\n"
        "6. Random movie\n"
        "7. Search movie\n"
        "8. Movies sorted by rating\n"
    )
    print(menu_text)


def get_choice():
    """
    Prompt the user to enter a choice from 0 to 8.
    Repeats until a valid integer in range is entered.
    """
    while True:
        print_menu()
        try:
            choice = int(input("Enter choice (0-8): "))
            if 0 <= choice <= 8:
                return choice
            print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")


def exit_program(*args):
    """Exit the program."""
    print("\nBye!")
    sys.exit(0)


def print_movie_info(movie_title, movie_data):
    """Print the data of a movie."""
    textline = movie_title + " - "
    for key, value in movie_data.items():
        textline += f"{key}: {value}; "
    print(textline[:-2])


def list_movies(movies):
    """Print all movies and their ratings."""
    print(f"\n{len(movies)} Movies in total")

    for title, data in movies.items():
        print_movie_info(title, data)


def add_movie(movies):
    """Add a new movie with a rating if it does not already exist."""
    while True:
        movie_title = input("\nEnter new movie title: ").strip()
        if movie_title:
            break
        else:
            print("Movie title can't be empty")

    if movie_title in movies:
        print(f"Movie {movie_title} already exists")
        return

    while True:
        try:
            rating = float(input("Enter new movie rating (0-10): "))
            if rating < 0 or rating > 10:
                raise ValueError
            break
        except ValueError:
            print("Invalid rating input. Please enter a number between 0 and 10.")

    while True:
        try:
            year_of_release = int(input("Enter new movie year of release: "))
            break
        except ValueError:
            print("Invalid year of release input, please enter an integer.")

    movie_storage.add_movie(movie_title, year_of_release, rating)
    print(f"Movie {movie_title} successfully added")


def delete_movie(movies):
    """Delete a movie if it exists."""
    movie_title = input("\nEnter movie title: ").strip()
    if movie_title in movies:
        movie_storage.delete_movie(movie_title)
        print(f"Movie {movie_title} successfully deleted")
    else:
        print("Movie not found")


def update_movie(movies):
    """Update the rating of an existing movie."""
    movie_title = input("\nEnter movie title to update: ").strip()

    if movie_title not in movies:
        print("Movie not found")
        return

    while True:
        try:
            rating = float(input("Enter new movie rating: "))
            if 0 <= rating <= 10:
                movie_storage.update_movie(movie_title, rating)
                print(f"Movie {movie_title} successfully updated")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid rating input. Please enter a number between 0 and 10.")


def get_stats(movies):
    """Print average, median, best, and worst movie ratings."""
    if not movies:
        print("No movies found")
        return

    ratings = [movie["rating"] for movie in movies.values()]
    avg_rating = sum(ratings) / len(ratings)
    median_rating = median(ratings)

    max_rating = max(ratings)
    min_rating = min(ratings)

    max_movies = [
        title for title, data in movies.items() if data["rating"] == max_rating
    ]
    min_movies = [
        title for title, data in movies.items() if data["rating"] == min_rating
    ]

    print(f"\nAverage rating: {avg_rating:.2f}")
    print(f"Median rating: {median_rating:.2f}")
    print(f"Best movie: {str(max_movies)[1:-1]}, {max_rating:.2f}")
    print(f"Worst movie: {str(min_movies)[1:-1]}, {min_rating:.2f}")


def print_random_movie(movies):
    """Print a randomly selected movie and its rating."""
    if not movies:
        print("No movies found")
        return
    movie_choice = random.choice(list(movies.items()))
    print("\nYour movie for tonight is ", end="")
    print_movie_info(movie_choice[0], movie_choice[1])


def search_movie(movies):
    """Search for movies containing a substring (case-insensitive)."""
    search_term = input("\nEnter part of movie title: ").strip().lower()
    found = False
    for title, data in movies.items():
        if search_term in title.lower():
            print_movie_info(title, data)
            found = True
    if not found:
        print("No movies found matching your search.")


def print_sorted_movies(movies):
    """Print movies sorted by rating in descending order."""
    print()
    if not movies:
        print("No movies found.")
        return
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
    for title, data in sorted_movies:
        print_movie_info(title, data)


def main():
    """Main program loop."""
    print("********** My Movies Database **********")

    commands = {
        0: exit_program,
        1: list_movies,
        2: add_movie,
        3: delete_movie,
        4: update_movie,
        5: get_stats,
        6: print_random_movie,
        7: search_movie,
        8: print_sorted_movies,
    }

    while True:
        choice = get_choice()
        if choice in commands:
            movies = movie_storage.get_movies()
            commands[choice](movies)
        else:
            raise ValueError("Invalid choice")
        input("\nPress Enter to continue")


if __name__ == "__main__":
    main()
