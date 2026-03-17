import requests
import time
from app import app
from models import db, Anime, Favorite

def fetch_top_anime(pages=8):
    """Fetches top anime from Jikan API. Each page has 25 anime."""
    print(f"Fetching top {pages * 25} anime from Jikan API. This may take a minute...")
    anime_list = []
    
    for page in range(1, pages + 1):
        print(f"Fetching page {page} of {pages}...")
        try:
            response = requests.get(f"https://api.jikan.moe/v4/top/anime?page={page}")
            if response.status_code == 200:
                data = response.json()
                for item in data.get('data', []):
                    title = item.get('title_english') or item.get('title')
                    
                    # Extract primary genre
                    genres = item.get('genres', [])
                    genre_name = genres[0]['name'] if genres else "Unknown"
                    
                    # Truncate synopsis if it's too long
                    description = item.get('synopsis', 'No description available.')
                    if description and len(description) > 1000:
                        description = description[:997] + "..."
                        
                    image_url = item['images']['jpg']['large_image_url']
                    
                    episodes = item.get('episodes') or 0
                    rating = item.get('score') or 0.0
                    
                    anime_list.append({
                        "title": title,
                        "genre": genre_name,
                        "episodes": episodes,
                        "rating": float(rating),
                        "description": description,
                        "image_url": image_url
                    })
            else:
                print(f"Failed to fetch page {page}: Status {response.status_code}")
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            
        time.sleep(1.5) # Jikan API rate limit is heavily restricted (around 3 requests per second, but 1 request/sec is safer)
        
    return anime_list

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        print("Clearing existing anime data to avoid duplicates...")
        for fav in Favorite.query.all():
            db.session.delete(fav)
        for anime in Anime.query.all():
            db.session.delete(anime)
        db.session.commit()
        
        # You can change the 'pages' argument to fetch more. 16 pages = 400 anime.
        new_anime_data = fetch_top_anime(pages=16)
        
        print(f"\nSaving {len(new_anime_data)} anime to the local database...")
        for data in new_anime_data:
             # Just in case there's duplicate titles at the same rank
             if not Anime.query.filter_by(title=data['title']).first():
                anime = Anime(**data)
                db.session.add(anime)
            
        db.session.commit()
        print("Success! Database has been populated with a large collection of anime.")
