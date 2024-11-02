# Get Ratings

Get the highest rated episode for each season of a TV show.

## Usage

```bash
python getratings.py
```

## Environment Variables

Create a `.env` file with the following:

- `OMDB_API_KEY`: The API key for the OMDb API.

Get a free API key from [OMDb API](https://www.omdbapi.com/apikey.aspx).

## Example

```bash
python getratings.py
```

### Output

```bash
Enter the show name: the americans
Verbose? (y/n): n

Fetching ratings for 'the americans'...
IMDb Rating: 8.4 (Votes: 114,008)

Highest rated episode for season 1: The Colonel (Rating: 9.0)
Highest rated episode for season 2: Echo (Rating: 8.9)
Highest rated episode for season 3: Stingers (Rating: 9.0)
Highest rated episode for season 4: Travel Agents (Rating: 8.9)
Highest rated episode for season 5: Dyatkovo (Rating: 8.7)
Highest rated episode for season 6: START (Rating: 9.7)
```
