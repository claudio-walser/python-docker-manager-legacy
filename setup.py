#!/usr/bin/env python3

from setuptools import setup, find_packages


def read(fpath):
    with open(fpath, 'r') as f:
        return f.read()


def version(fpath):
    return read(fpath).strip()

setup(
    name='docker-manager',
    version=version('version.txt'),
    description='Tool for docker container management',
    author='Claudio Walser',
    long_description=read('README.rst'),
    author_email='claudio.walser@srf.ch',
    url='https://github.com/claudio-walser/python-docker-manager',
    packages=find_packages(),
    install_requires=['simple-cli', 'pyyaml', 'argparse', 'argcomplete', 'shutilwhich'],
    entry_points={
        'console_scripts': [
            'docker-image = dockerManager.bin.image:main',
            'docker-container = dockerManager.bin.container:main',
            'docker-watcher = dockerManager.bin.watcher:main',
            'docker-bridge = dockerManager.bin.bridge:main'
        ]
    },
    license='Apache License',
    keywords=['docker', 'application', 'docker-manager', 'docker-compose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
