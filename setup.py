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
        msg = "%s is not installed. Install your test requirments." % err_msg
        raise ImportError(msg)
    os.system('py.test tests')
    sys.exit()

setup(name="beluga",
      version="0.1",
      description="A trajectory optimization framework",
      author="Michael J. Grant",
      author_email='mjgrant@purdue.edu',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      license="",
      url="http://github.rcac.purdue.edu/RDSL/beluga",
      py_modules=['beluga'],
      packages=find_packages(exclude=['docs', 'tests*', 'sandbox', 'examples']),
    #   scripts=['bin/beluga'],
      entry_points={
          'console_scripts': [
              'beluga = beluga.__main__:main'
          ]
      },
      install_requires=[
        "dill",
        "numpy",
        "sympy",
        "scipy",
        "pytest",
        "pytest-cov",
        "pytest-describe",
        "coverage",
    	"mock",
        "matplotlib",
        "numexpr",
        "pystache",
        "docopt",
        "multiprocessing_on_dill",
      ]
      )
