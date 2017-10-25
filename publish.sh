#!/bin/bash

rm -rf dist/ build/ docker-manager.egg-info/
python3 setup.py bdist_wheel
twine upload dist/*
