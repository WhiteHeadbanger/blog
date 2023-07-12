from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config import config
from database.db import db

app = Flask(__name__)
_bcrypt = Bcrypt(app)

# Routes
from routes import blog, auth

if __name__ == '__main__':
    # Config
    app.config.from_object(config['development'])

    #database
    db.init_app(app)

    # Flask-login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models.UserModel import UserModel
    
    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(user_id)

    # Migrate
    migrate = Migrate(app, db)

    # Blueprints
    app.register_blueprint(blog.main, url_prefix='/blog')
    app.register_blueprint(auth.auth, url_prefix='/auth')

    print(app.blueprints, flush=True)

    app.run()