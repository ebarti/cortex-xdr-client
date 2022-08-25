#!/usr/bin/env bash

set -e

VERSION=$1
echo "Ensuring we are on master branch"
git checkout master
echo "Updating to version $VERSION"
poetry version $VERSION
echo "Commiting version change"
git add pyproject.toml
git commit -m "Bump to v$VERSION"
git push
echo "Updating tag to v$VERSION"
git tag v$VERSION
echo "Pushing tag to origin"
git push --tags