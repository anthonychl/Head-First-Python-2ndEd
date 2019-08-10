from flask import session
from functools import wraps # important to import everytime we are creating our own decorators

def check_logged_in(func):
    @wraps(func) #use wraps to decorate wrapper
    def wrapper(*args, **kwargs): #make sure that wrapper accepts any number and type of arguments
        if 'logged_in' in session: #if the user's browser is logged in
            return func(*args, **kwargs)   #invoke the decorated function, using the same arguments passed to wrapper
        return 'You are NOT logged in' #if the user's browser inst logged in return an appropriate message
    return wrapper #return the nested function