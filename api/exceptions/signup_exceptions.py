class SignUpUserAlreadyExistsError(Exception):
    def __init__(self, message):            
        super().__init__(message)

class SignUpPasswordsDontMatchError(Exception):
    def __init__(self, message):            
        super().__init__(message)