import Cli

class Container(object):

  id = False
  name = False
  isStarted = False
  isCreated = False
  settings = {}

  def __init__(self, name, settings):
    self.name = name
    self.settings = settings
    self.interface = Cli.Interface()

  def status(self):
    self.interface.header("Status of %s" % self.name)

  def start(self):
    self.interface.header("Start %s" % self.name)

  def stop(self):
    self.interface.header("Stop %s" % self.name)

  def restart(self):
    self.interface.header("Restart %s" % self.name)

  def destroy(self):
    self.interface.header("Destroy %s" % self.name)
