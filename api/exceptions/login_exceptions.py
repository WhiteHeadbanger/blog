class LoginUserNotFoundError(Exception):
    def __init__(self, message):            
        super().__init__(message)

class LoginWrongPasswordError(Exception):
    def __init__(self, message):            
        super().__init__(message)