# Source: http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
def static_var(varname, value):
    """Decorator that defines a static variable inside a function"""
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate
