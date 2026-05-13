# Movies App

A simple CLI application for managing your movie collection with database storage and HTML website generation.

## Features

- **Add/manage movies** – Add, delete, and update movies in your personal database
- **Search & sort** – Search movies and sort by rating
- **Statistics** – View collection stats (median rating, movie count, etc.)
- **Website generation** – Generate an HTML website displaying your movie posters and ratings
- **OMDb integration** – Fetch real movie data (poster, year, rating) from the OMDb API

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your OMDb API key (get one free at https://www.omdbapi.com/):
   ```
   API_KEY=your_api_key_here
   ```

## Usage

Run the application:
```bash
python main.py
```

Then select from the menu:
- List, add, delete, or update movies
- View statistics and search
- Get random recommendations
- Generate an HTML website of your collection
