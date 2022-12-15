from models.queries import get_user_by_username, create_user
from exceptions.signup_exceptions import SignUpPasswordsDontMatchError, SignUpUserAlreadyExistsError
from exceptions.login_exceptions import LoginUserNotFoundError, LoginWrongPasswordError

class UserController:

    @classmethod
    def signup(cls, data):
        username = data['username']
        password = data['password']
        password_confirmation = data['password-confirmation']

        user = get_user_by_username(username)
        if user:
            raise SignUpUserAlreadyExistsError(message = f"Username {username} already exists!")
        
        if password != password_confirmation:
            raise SignUpPasswordsDontMatchError(message = "Passwords don't match!")
        
        user = create_user(username, password)

        return user.serialize()
    
    @classmethod
    def login(cls, data):
        username = data['username']
        password = data['password']

        user = get_user_by_username(username)
        if not user:
            raise LoginUserNotFoundError(message = f"Username {username} doesn't exist!")
        
        if password != user.password:
            raise LoginWrongPasswordError(message = "Passwords don't match!")
        
        return user

    @classmethod
    def logout(cls):
        pass