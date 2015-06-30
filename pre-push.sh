#!/bin/sh
# pre-commit.sh
# Run the following command to install the git pre-commit hook
#     ln -s ../../pre-push.sh .git/hooks/pre-push

# Stash any uncommited changes
git stash -q --keep-index

# Test prospective commit
./run_tests.sh
RESULT=$?

# Put back uncommited changes
git stash pop -q

# Stop commit if tests fail
[ $RESULT -ne 0 ] && exit 1

exit 0
