import os

def get_root():
    import beluga
    return os.path.dirname(beluga.__file__)
