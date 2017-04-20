#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import sys
import os
import argcomplete
import argparse
import Cli

from dockerManager.Config import Config
from dockerManager.Container import Container


interface = Cli.Interface()


if len(sys.argv) != 2:
    interface.error("Argument error - Only one parameter -configfile is needed!")
    sys.exit(1)

# create parser in order to autocomplete
parser = argparse.ArgumentParser()

parser.add_argument(
    'configfile',
    help = "Where is you desired config file?",
    type = str
)

argcomplete.autocomplete(parser)

def main():
  arguments = parser.parse_args()
  configFile = arguments.configfile
  if not os.path.isfile(configFile):
    interface.error('Argument error - your config file is not found!')
    sys.exit(1)

  try:
    config = Config('.docker-manager')
    config.load()
  except:
    interface.error('Config error - could not parse your given config file!')
    sys.exit(1)


  names =  config.getContainerNames()
  for name in names:
    settings = config.getContainerSettings(name)
    for i in range(0, settings['maxContainers']):
      containerName = "%s-%s" % (name, i)
      container = Container(containerName, settings)
      print(container.getIpAddress())

  sys.exit(0)
  