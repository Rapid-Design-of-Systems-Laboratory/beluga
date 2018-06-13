from setuptools import find_packages, setup
import os, sys

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

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

modules = ['beluga.bvpsol',
           'beluga.codegen',
           'beluga.continuation',
           'beluga.ivpsol',
           'beluga.ivpsol.integrators',
           'beluga.optimlib',
           'beluga.utils']

tests = ['beluga.bvpsol.tests',
         'beluga.continuation.tests',
         'beluga.ivpsol.tests',
         'beluga.ivpsol.integrators.tests',
         'beluga.optimlib.tests']

setup(name="beluga",
      version="0.1.4",
      description="An indirect trajectory optimization framework.",
      author="Michael Sparapany",
      author_email='msparapa@purdue.edu',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      license="MIT",
      url="https://github.com/Rapid-Design-of-Systems-Laboratory/beluga",
      py_modules=['beluga'],
      packages=['beluga'] + modules + tests,
    #   scripts=['bin/beluga'],
      entry_points={
          'console_scripts': [
              'beluga = beluga.__main__:main'
          ]
      },
      install_requires=requirements,
      include_package_data = True
      )
