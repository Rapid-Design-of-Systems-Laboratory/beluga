#!/usr/bin/env bash

cd ..

python setup.py sdist
python setup.py bdist_wheel
