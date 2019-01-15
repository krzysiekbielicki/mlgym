#!/bin/sh

sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
brew install pyenv
pyenv install 3.6.5
pipenv install --python ~/.pyenv/versions/3.6.5/bin/python3
pipenv shell
