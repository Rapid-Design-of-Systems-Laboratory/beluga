#!/usr/bin/env bash

cd ..

python -m pytest beluga/

read -n 1 -s -r -p "Press any key to exit"
