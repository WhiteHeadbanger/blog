from flask import Flask, jsonify
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config
from database.db import db

# Routes
from routes import blog, auth

app = Flask(__name__)


""" login_manager = LoginManager()
login_manager.login_view = 'auth.login' """

if __name__ == '__main__':
    # Config
    app.config.from_object(config['development'])

    #database
    db.init_app(app)
    
    # Migrate
    migrate = Migrate(app, db)

    # Blueprints
    app.register_blueprint(blog.main, url_prefix='/api/blog')
    app.register_blueprint(auth.auth, url_prefix='/api/auth')
    app.run()