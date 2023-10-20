from app import _bcrypt
from models.queries import get_user_by_username, create_user, get_user_by_uid
from exceptions.signup_exceptions import SignUpPasswordsDontMatchError, SignUpUserAlreadyExistsError
from exceptions.login_exceptions import LoginUserNotFoundError, LoginWrongPasswordError

class UserController:

    @classmethod
    def signup(cls, data):
        username = data['username']
        password = data['password']
        first_name = data['first-name']
        last_name = data['last-name']
        password_confirmation = data['password-confirmation']

        user = get_user_by_username(username)
        if user:
            raise SignUpUserAlreadyExistsError(message = f"Username {username} already exists!")
        
        if password != password_confirmation:
            raise SignUpPasswordsDontMatchError(message = "Passwords don't match!")
        
        encrypted_password = _bcrypt.generate_password_hash(password).decode('utf-8')
        user = create_user(username, first_name, last_name, encrypted_password)

        return user.serialize()
    
    @classmethod
    def login(cls, data):
        username = data['username']
        password = data['password']

        user = get_user_by_username(username)
        if not user:
            raise LoginUserNotFoundError(message = f"Username {username} doesn't exist!")
        
        if not _bcrypt.check_password_hash(user.password, password):
            raise LoginWrongPasswordError(message = "Passwords don't match!")
        
        return user

    @classmethod
    def logout(cls):
        pass

    @classmethod
    def get_user(cls, user_id):
        return get_user_by_uid(user_id)