#! /usr/bin/env sh
set -euo pipefail

# Adjust paths to be relative to the frontend directory
# shellcheck disable=SC2124
FILES=$@

# Run Prettier with the adjusted paths
# shellcheck disable=SC2086
npx prettier --write $FILES
