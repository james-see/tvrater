import os
import requests
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

def get_show_details(show_name, api_key):
    encoded_show_name = quote_plus(show_name)
    url = f'http://www.omdbapi.com/?apikey={api_key}&t={encoded_show_name}&type=series'
    response = requests.get(url)
    data = response.json()
    if data.get('Response') == 'True':
        imdb_id = data['imdbID']
        total_seasons = int(data['totalSeasons'])
        imdb_rating = data.get('imdbRating', 'N/A')
        imdb_votes = data.get('imdbVotes', 'N/A')
        return imdb_id, total_seasons, imdb_rating, imdb_votes
    else:
        print(f"Error: {data.get('Error')}")
        return None, None, None, None

def get_episode_ratings(imdb_id, total_seasons, api_key, verbose):
    for season in range(1, total_seasons + 1):
        url = f'http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}&Season={season}'
        response = requests.get(url)
        data = response.json()
        if data.get('Response') == 'True':
            episodes = data.get('Episodes', [])
            highest_rated = max(episodes, key=lambda x: float(x['imdbRating']) if x['imdbRating'] != 'N/A' else 0)
            print(f"Highest rated episode for season {season}: {highest_rated['Title']} (Rating: {highest_rated['imdbRating']})")
            
            if verbose == 'y':
                for episode in episodes:
                    print(f"Season {season}, Episode {episode['Episode']}: {episode['Title']}")
                    print(f"Rating: {episode['imdbRating']} \n")
        else:
            print(f"Error retrieving season {season}: {data.get('Error')}")

def main():
    api_key = os.getenv('OMDB_API_KEY')
    if not api_key:
        print("Error: The OMDB_API_KEY environment variable is not set.")
        print("Please set the environment variable and try again.")
        return

    show_name = input("Enter the show name: ").strip()
    verbose = input("Verbose? (y/n): ").strip()
    imdb_id, total_seasons, imdb_rating, imdb_votes = get_show_details(show_name, api_key)
    
    if not imdb_id:
        print("Failed to retrieve show details.")
        return

    print(f"\nFetching ratings for '{show_name}'...")
    print(f"IMDb Rating: {imdb_rating} (Votes: {imdb_votes})\n")

    get_episode_ratings(imdb_id, total_seasons, api_key, verbose)

if __name__ == "__main__":
    main()
