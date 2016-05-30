# Ref: http://stackoverflow.com/a/22348885/538379
import signal
class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

    # Function decorator version (untested)
    # Ref: http://stackoverflow.com/a/2282656/538379
    @staticmethod
    def timeout(seconds = 1, error_message='TimeOut'):
        def decorator(func):
            def wrapper(*args, **kwargs):
                with timeout(seconds, error_message):
                    result = func(*args, **kwargs)
                return result

            return wraps(func)(wrapper)

        return decorator
