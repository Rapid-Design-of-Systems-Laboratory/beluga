from setuptools import find_packages, setup
import os
import sys

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('requirements_dev.txt') as f:
    requirements_dev = f.read().splitlines()

long_description = '''beluga is a general purpose indirect trajectory optimization framework.'''

modules = ['beluga.bvpsol',
           'beluga.bvpsol._bvp',
           'beluga.bvpsol._shooting',
           'beluga.codegen',
           'beluga.continuation',
           'beluga.ivpsol',
           'beluga.optimlib',
           'beluga.utils']

tests = ['beluga.bvpsol.tests',
         'beluga.ivpsol.tests',
         'beluga.optimlib.tests']

dir_setup = os.path.dirname(os.path.realpath(__file__))

__version__ = None
with open(os.path.join(dir_setup, 'beluga', 'release.py')) as f:
    # Defines __version__
    exec(f.read())

setup(name="beluga",
      version=__version__,
      description="A general purpose indirect trajectory optimization framework.",
      long_description=long_description,
      author="Michael Sparapany",
      author_email='msparapa@purdue.edu',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      python_requires='>3.5',
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics'
      )
      )
