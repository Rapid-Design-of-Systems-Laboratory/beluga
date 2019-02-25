from setuptools import find_packages, setup
import os, sys

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

long_description = '''beluga is a unified direct and indirect trajectory optimization library.'''

modules = ['beluga.bvpsol',
           'beluga.bvpsol.collocation',
           'beluga.codegen',
           'beluga.continuation',
           'beluga.continuation.strategies',
           'beluga.ivpsol',
           'beluga.ivpsol.integrators',
           'beluga.liepack',
           'beluga.liepack.domain.hspaces',
           'beluga.liepack.domain.liealgebras',
           'beluga.liepack.domain.liegroups',
           'beluga.liepack.field',
           'beluga.optimlib',
           'beluga.utils']

tests = ['beluga.bvpsol.tests',
         'beluga.ivpsol.tests',
         'beluga.liepack.domain.liealgebras.tests',
         'beluga.liepack.domain.liegroups.tests',
         'beluga.liepack.tests',
         'beluga.optimlib.tests']

dir_setup = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_setup, 'beluga', 'release.py')) as f:
    # Defines __version__
    exec(f.read())

setup(name="beluga",
      version=__version__,
      description="An indirect trajectory optimization framework.",
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
      include_package_data = True,
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
