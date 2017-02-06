import os
import yaml

from pprint import pprint

class Config:

  yaml = {}
  filename = '.docker-manager'

  def __init__(self, filename):
    if not os.path.isfile(filename):
      raise Exception("File %s not found" % filename)
    self.filename = filename

  def load(self):
    with open(self.filename, 'r') as stream:
      self.yaml = yaml.safe_load(stream)
      return True
    return False

  def getContainerNames(self):
    return list(self.yaml['container'].keys())

  def getContainerSettings(self, name):
    return self.yaml['container'][name]
