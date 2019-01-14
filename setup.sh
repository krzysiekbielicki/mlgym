#!/bin/sh

pip3 install --upgrade virtualenv
virtualenv --system-site-packages -p python3 venv
# Activate the Virtualenv environment
source ./venv/bin/activate
# Install TensorFlow and all the packages
pip3 install --upgrade tensorflow
#Install Keras
pip3 install keras
pip3 install gym-super-mario-bros
