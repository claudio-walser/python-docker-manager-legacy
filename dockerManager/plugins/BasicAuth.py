import os
import Cli
from dockerManager.plugins.AbstractPlugin import AbstractPlugin

class BasicAuth(AbstractPlugin):

  cli = Cli.Command()
  basePath = '/etc/nginx/basic_auth.d'

  def write(self):
    if os.path.isfile("%s/%s" % (self.basePath, self.name)):
      print("Password for %s already set" % (self.name))
      return False

    if 'password' in self.settings['nginx'] and self.settings['nginx']['password'] == '<pwgen>':
      pw = self.cli.execute("pwgen --capitalize --numerals --symbols -1 32 1")
    elif 'password' in self.settings['nginx']:
      pw = self.settings['nginx']['password']
    else:
      return False;

    self.cli.execute("printf \"%s:$(openssl passwd -crypt '%s')\" > %s/%s" % (self.name, pw, self.basePath, self.name))
    print("%s:%s" % (self.name, pw))
    return True

  def remove(self):
    if os.path.isfile("%s/%s" % (self.basePath, self.name)):
      self.cli.execute("rm  %s/%s" % (self.basePath, self.name))


  # callable methods
  def start(self):
    # should optimize and do that only on creation of the container
    self.write()
    pass

  def destroy(self):
    self.remove()
    pass
