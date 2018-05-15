from setuptools import find_packages, setup
import os, sys
# Run tests
# Ref: http://www.pydanny.com/python-dot-py-tricks.html
if sys.argv[-1] == 'test':
    test_requirements = [
        'pytest',
        'pytest-cov',
        'pytest-describe',
        'coverage',
	    'mock'
    ]
    try:
        modules = map(__import__, test_requirements)
    except ImportError as e:
        err_msg = e.message.replace("No module named ", "")
        msg = "%s is not installed. Install your test requirements." % err_msg
        raise ImportError(msg)
    os.system('py.test tests')
    sys.exit()

setup(name="beluga",
      version="0.1.0",
      description="An indirect trajectory optimization framework",
      author="Michael Sparapany",
      author_email='msparapa@purdue.edu',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      license="MIT",
      url="https://github.com/Rapid-Design-of-Systems-Laboratory/beluga",
      py_modules=['beluga'],
      packages=find_packages(exclude=['docs', 'tests*', 'sandbox', 'examples']),
    #   scripts=['bin/beluga'],
      entry_points={
          'console_scripts': [
              'beluga = beluga.__main__:main'
          ]
      }
      )
