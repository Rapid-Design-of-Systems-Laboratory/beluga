from setuptools import find_packages, setup
import os, sys

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.rst') as file:
    long_description = file.read()

modules = ['beluga.bvpsol',
           'beluga.codegen',
           'beluga.continuation',
           'beluga.ivpsol',
           'beluga.ivpsol.integrators',
           'beluga.optimlib',
           'beluga.utils']

tests = ['beluga.bvpsol.tests',
         'beluga.ivpsol.tests',
         'beluga.ivpsol.integrators.tests',
         'beluga.optimlib.tests']

setup(name="beluga",
      version="0.1.5",
      description="An indirect trajectory optimization framework.",
      long_description=long_description,
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
