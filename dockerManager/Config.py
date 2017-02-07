import os
import yaml


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

  def getDefaultContainerSettings(self):
    return self.yaml['containerDefaults']

  def getContainerSettings(self, name):
    settings = self.getDefaultContainerSettings()
    settings.update(self.yaml['container'][name])
    return settings
