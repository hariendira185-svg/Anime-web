from flask import Flask, render_template, redirect, url_for, flash, request
from models import db, User, Anime, Favorite
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'anime_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    query = request.args.get('q')
    genre = request.args.get('genre')
    
    animes = Anime.query
    if query:
        animes = animes.filter(Anime.title.ilike(f'%{query}%'))
    if genre and genre != 'All':
        animes = animes.filter_by(genre=genre)
        
    animes = animes.all()
    
    genres = db.session.query(Anime.genre).distinct().all()
    genres = [g[0] for g in genres]
    
    return render_template('index.html', animes=animes, genres=genres)

@app.route('/anime/<int:anime_id>')
def anime_detail(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    is_favorite = False
    if current_user.is_authenticated:
        fav = Favorite.query.filter_by(user_id=current_user.id, anime_id=anime_id).first()
        if fav:
            is_favorite = True
            
    return render_template('anime_detail.html', anime=anime, is_favorite=is_favorite)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_exists = User.query.filter_by(username=username).first()
        email_exists = User.query.filter_by(email=email).first()
        
        if user_exists:
            flash('Username already exists.', 'danger')
        elif email_exists:
            flash('Email already registered.', 'danger')
        else:
            # Explicitly specify pbkdf2 as Werkzeug uses this format often
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Please login.', 'success')
            return redirect(url_for('login'))
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('index'))

@app.route('/add_favorite/<int:anime_id>', methods=['POST'])
@login_required
def add_favorite(anime_id):
    fav = Favorite.query.filter_by(user_id=current_user.id, anime_id=anime_id).first()
    if not fav:
        new_fav = Favorite(user_id=current_user.id, anime_id=anime_id)
        db.session.add(new_fav)
        db.session.commit()
        flash('Added to favorites!', 'success')
    return redirect(url_for('anime_detail', anime_id=anime_id))

@app.route('/remove_favorite/<int:anime_id>', methods=['POST'])
@login_required
def remove_favorite(anime_id):
    fav = Favorite.query.filter_by(user_id=current_user.id, anime_id=anime_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        flash('Removed from favorites!', 'info')
    
    if request.referrer and 'dashboard' in request.referrer:
        return redirect(url_for('dashboard'))
    return redirect(url_for('anime_detail', anime_id=anime_id))

@app.route('/dashboard')
@login_required
def dashboard():
    favorites = Favorite.query.filter_by(user_id=current_user.id).all()
    favorite_animes = [fav.anime for fav in favorites]
    return render_template('dashboard.html', animes=favorite_animes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
