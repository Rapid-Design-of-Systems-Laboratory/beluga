from setuptools import find_packages, setup
import os
import sys

dir_setup = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_setup, 'beluga', 'release.py')) as f:
    exec(f.read())

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('requirements_dev.txt') as f:
    requirements_dev = f.read().splitlines()

long_description = '''beluga is a general purpose indirect trajectory optimization framework.'''

modules = ['beluga.continuation',
           'beluga.compilation',
           'beluga.symbolic_manipulation',
           'beluga.utils']

# tests = ['beluga.bvp_solvers.tests',
#          'beluga.ivp_solvers.tests',
#          'beluga.optimlib.tests']

tests = []

dir_setup = os.path.dirname(os.path.realpath(__file__))

setup(name="beluga",
      version=__version__,
      description="A general purpose indirect trajectory optimization framework.",
      long_description=long_description,
      author="Sean Nolan",
      author_email='nolans@pudue.edu',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      python_requires='>3.6',
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
      extras_require={'dev': requirements_dev},
      include_package_data=True,
      classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics'
      )
      )
