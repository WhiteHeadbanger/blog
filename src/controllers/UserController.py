from models.queries import get_user_by_username, create_user

class UserController:

    @classmethod
    def signup(cls, data):
        username = data['username']
        password = data['password']
        password_confirmation = data['password_confirmation']

        user = get_user_by_username(username)
        if user:
            return {"data": f"Username {username} already exists!"}
        
        if password != password_confirmation:
            return {"data": "Passwords don't match!"}
        
        user = create_user(username, password)

        return user.serialize()
    
    @classmethod
    def login(cls, data):
        username = data['username']
        password = data['password']

        user = get_user_by_username(username)
        if not user:
            return {"data": f"Username {username} doesn't exist!"}
        
        if password != user.password:
            return {"data": "Passwords don't match!"}
        
        return user

    @classmethod
    def logout(cls):
        pass