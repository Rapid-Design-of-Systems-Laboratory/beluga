from time import time
_tstart_stack = []

def tic():
    _tstart_stack.append(time())

def toc(show=False,fmt="Elapsed: %s s"):
    if show:
        print fmt % (time() - _tstart_stack.pop())
    else:
        return (time() - _tstart_stack.pop())
