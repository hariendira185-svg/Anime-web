# Anime Favorites Web Application

A Flask-based web application where users can discover new anime, view details, and manage their personal favorites list.

## Features
- User Authentication (Register, Login, Logout)
- View Anime List and Details
- Search Anime by Title
- Filter Anime by Genre
- Add/Remove Anime to personal Favorites
- User Dashboard
- Dark Mode support

## How to Run in VS Code

1. **Open the project folder (`anime_favorites`) in VS Code.**
2. **Create a virtual environment:**
   - Open a new terminal in VS Code (`Terminal > New Terminal`)
   - Run: `python -m venv venv`
3. **Activate the virtual environment:**
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. **Install the dependencies:**
   - Run: `pip install -r requirements.txt`
5. **Initialize the database and seed data:**
   - Run: `python seed.py`
6. **Run the application:**
   - Run: `python app.py`
7. **Open in Browser:**
   - Go to `http://127.0.0.1:5000/` to view the application!

## Tech Stack
- **Backend:** Python, Flask, SQLAlchemy, Flask-Login
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
