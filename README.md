📺 Anime Favorites Web App
📌 Project Overview

This is a full-stack Anime Favorites Web Application built using Python Flask. The application allows users to explore anime, view details, and manage their personal favorite anime list.

🚀 Features

🔐 User Authentication (Register/Login/Logout)

📚 Browse Anime List

🔍 Search Anime by Name

📄 View Anime Details (title, genre, episodes, rating, description, image)

❤️ Add/Remove Anime from Favorites

📊 Personalized User Dashboard

🎨 Responsive UI Design

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript, Bootstrap

Backend: Python (Flask)

Database: SQLite

📁 Project Structure
anime-site/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── anime_detail.html
│   └── favorites.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
⚙️ Installation & Setup (Step-by-Step)
1️⃣ Clone the Repository
git clone https://github.com/your-username/anime-site.git
cd anime-site
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python app.py
5️⃣ Open in Browser

Go to:

http://127.0.0.1:5000/
🗄️ Database Schema
Users Table

id

username

email

password

Anime Table

id

title

genre

episodes

rating

description

image_url

Favorites Table

id

user_id

anime_id

✨ How to Use

Register a new account

Login to your account

Browse anime list

Click on any anime to view details

Add anime to favorites ❤️

View your favorites in dashboard

Remove anime anytime

💡 Future Improvements

⭐ Anime rating system

💬 Comments/Reviews

🎥 Trailer integration (YouTube)

🌙 Dark mode

🤖 Anime recommendation system

🌐 API integration (MyAnimeList / Jikan API)

🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

📜 License

This project is open-source and available.

👨‍💻 Author

Hariendira


Hari Endira
