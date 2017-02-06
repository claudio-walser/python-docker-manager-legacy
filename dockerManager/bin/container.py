#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import sys
import os
import argcomplete
import argparse
import Cli

from dockerManager.Config import Config
from dockerManager.Container import Container

from pprint import pprint

interface = Cli.Interface()
if not os.path.isfile('.docker-manager'):
    interface.error('No .docker-manager file found in this directory!')
    sys.exit(1)

config = Config('.docker-manager')
config.load()

# create parser in order to autocomplete
parser = argparse.ArgumentParser()

parser.add_argument(
    'command',
    help = "What command do you want to execute?",
    type = str,
    choices = [
        "status",
        "start",
        "stop",
        "restart",
        "destroy"
    ]
)

parser.add_argument(
    'name',
    help = 'Which container you want to execute the command on?',
    choices = config.getContainerNames(),
    type = str
)


argcomplete.autocomplete(parser)

def main():
  arguments = parser.parse_args()
  settings = config.getContainerSettings(arguments.name)

  for i in range(0, settings['maxContainers']):
    name = "%s-%s" % (arguments.name, i)
    container = Container(name, settings)

    result = False
    try:
      methodToCall = getattr(container, arguments.command)
      result = methodToCall() 
    except:
      interface.error('Container command %s not found!' % arguments.command)
      sys.exit(1)


  
  pprint(arguments)
