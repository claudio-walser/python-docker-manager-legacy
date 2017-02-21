import os
import Cli


class BasicAuth(object):

  cli = Cli()
  basePath = '/etc/nginx/basic_auth.d'


  def __init__(self, containerName, settings):
    self.containerName = containerName
    self.settings = settings

  def write(self, containerName):
    
    if 'password' in self.settings['nginx'] and self.settings['nginx']['password'] == '<pwgen>':
      pw = self.cli.execute("pwgen --capitalize --numerals --symbols -1 32 1")
    elif 'password' in self.settings['nginx']:
      pw = self.settings['nginx']['password']

    self.cli.execute("printf \"%s:$(openssl passwd -crypt '%s')\" > %s/%s" % (containerName, pw, self.basePath, containerName))
    print("%s:%s" % (containerName, pw))

  def remove(self, containerName):
    self.cli.execute("rm  %s/%s" % (self.basePath, containerName))


  # callable methods
  def status(self):
    pass

  def start(self):
    # should optimize and do that only on creation of the container
    self.write()
    pass

  def stop(self):
    pass

  def restart(self):
    pass

  def destroy(self):
    self.remove()
    pass
