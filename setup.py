from setuptools import find_packages, setup
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
      scripts=['bin/beluga'],
      install_requires=[
        "dill",
        "numpy",
        "sympy",
        "scipy",
        "pytest",
        "matplotlib",
        "pytest-cov",
        "numexpr",
        "pystache",
        "docopt",
        "multiprocessing_on_dill",
      ]
      )
