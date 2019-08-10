from functools import wraps # important to import everytime we are creating our own decorators

def decorator_name(func):
    @wraps(func) #use wraps to decorate wrapper
    def wrapper(*args, **kwargs): #make sure that wrapper accepts any number and type of arguments
        # code to execute BEFORE calling the decorated function
            return func(*args, **kwargs)   #invoke the decorated function, using the same arguments passed to wrapper
        # code to execute INSTEAD OF calling the decorated function
    return wrapper #return the nested function