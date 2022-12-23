import requests
import json

def get_movies(api_key, page_number):
    """
    Send HTTP request to TMDB API to get a list of movies.

    Parameters:
        api_key (str): TMDB API key.
        page_number (int): Page number to retrieve.

    Returns:
        list: List of movies.
    """
    # Send HTTP request to TMDB API
    response = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&page={page_number}')

    # Parse response as JSON
    movies = response.json()['results']
    for m in movies:
        print(m)
    return movies


def main():
    # TMDB API key
    api_key = '38d7bb69693fe6fc0448506e928553ed'

    # Number of pages to retrieve
    num_pages = 50

    # Initialize list to store movies
    movies = []

    # Get movies for each page
    for page in range(1, num_pages + 1):
        movies += get_movies(api_key, page)

    # Write movies to file
    with open('/Users/lq/PycharmProjects/DeAirFlowProject/data/raw/movies.json', 'w') as f:
        json.dump(movies, f)


if __name__ == "__main__":
    main()
