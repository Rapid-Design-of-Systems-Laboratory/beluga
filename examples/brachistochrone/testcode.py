import inspect
import functools

def test(a):
    yield 2*a

print('isgeneratorfunction(test):', inspect.isgeneratorfunction(test))
test2 = functools.partial(test, a=10)
print('isgenereatorfunction(test2):', inspect.isgeneratorfunction(test2))

