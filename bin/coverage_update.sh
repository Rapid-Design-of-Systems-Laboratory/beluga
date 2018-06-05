#!/usr/bin/env bash
# This script will automatically run coverage and regenerate the badge
# This required `coverage` and `coverage_badge`, which are not included in the `beluga` setup

# Move up 1 level. This file is currently in beluga/bin
cd ..

# Run pytest but only for files in beluga/ since we don't want to include full examples
coverage run -m pytest beluga/

# Display the report to the command window
coverage report -m

# Save the badge
coverage-badge -f -o coverage.svg
