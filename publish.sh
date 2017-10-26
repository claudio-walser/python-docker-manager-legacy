#!/bin/bash

rm -rf dist/ build/ docker_manager.egg-info/
python3 setup.py bdist_wheel
twine upload dist/*
