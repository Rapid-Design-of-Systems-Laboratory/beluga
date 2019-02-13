#!/bin/bash

cd ..
asv run
# If any errors come up, run this instead
# asv run --show-stderr

asv publish

asv preview

# Then visit http://127.0.0.1:8080
