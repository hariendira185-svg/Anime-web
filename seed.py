from app import app
from models import db, Anime

seed_data = [
    {
        "title": "Naruto",
        "genre": "Shonen",
        "episodes": 220,
        "rating": 8.3,
        "description": "Naruto Uzumaki, a mischievous adolescent ninja, struggles as he searches for recognition and dreams of becoming the Hokage, the village's leader and strongest ninja.",
        "image_url": "https://myanimelist.net/images/anime/1141/142503l.jpg"
    },
    {
        "title": "Attack on Titan",
        "genre": "Action",
        "episodes": 89,
        "rating": 9.0,
        "description": "After his hometown is destroyed and his mother is killed, young Eren Yeager vows to cleanse the earth of the giant humanoid Titans that have brought humanity to the brink of extinction.",
        "image_url": "https://myanimelist.net/images/anime/10/47347l.jpg"
    },
    {
        "title": "Death Note",
        "genre": "Thriller",
        "episodes": 37,
        "rating": 8.6,
        "description": "An intelligent high school student goes on a secret crusade to eliminate criminals from the world after discovering a notebook capable of killing anyone whose name is written into it.",
        "image_url": "https://myanimelist.net/images/anime/1079/138100l.jpg"
    },
    {
        "title": "My Hero Academia",
        "genre": "Shonen",
        "episodes": 138,
        "rating": 7.9,
        "description": "A superhero-loving boy without any powers is determined to enroll in a prestigious hero academy and learn what it really means to be a hero.",
        "image_url": "https://myanimelist.net/images/anime/10/78745l.jpg"
    },
    {
        "title": "Fullmetal Alchemist: Brotherhood",
        "genre": "Fantasy",
        "episodes": 64,
        "rating": 9.1,
        "description": "Two brothers search for a Philosopher's Stone after an attempt to revive their deceased mother goes awry and leaves them in damaged physical forms.",
        "image_url": "https://myanimelist.net/images/anime/1208/94745l.jpg"
    },
    {
        "title": "One Punch Man",
        "genre": "Comedy",
        "episodes": 24,
        "rating": 8.5,
        "description": "The story of Saitama, a hero that does it just for fun & can defeat his enemies with a single punch.",
        "image_url": "https://myanimelist.net/images/anime/12/76049l.jpg"
    }
]

with app.app_context():
    db.create_all()
    # Delete existing anime entries to update with high-res images
    for anime in Anime.query.all():
        db.session.delete(anime)
    db.session.commit()
    
    for data in seed_data:
        anime = Anime(**data)
        db.session.add(anime)
    db.session.commit()
    print("Database seeded with high-quality sample anime data!")
