import os
import Cli


class Nginx(object):

  settings = None
  name = None
  confd = '/etc/nginx/conf.d'

  def __init__(self, name, settings):
    self.name = name
    self.settings = settings

  def writeUpstreamConfig(self):
    upstreamString = 'upstream %s {\n' % self.name
    for i in range(0, self.settings['maxContainers']):
      upstreamString += '    server %s-%s' % (self.name, i)
      if 'backendPort' in self.settings['nginx']:
        upstreamString += ':%s' % (self.settings['nginx']['backendPort'])
      upstreamString += ';\n'

    upstreamString += '}'

    filename = '%s/upstream-%s.conf' % (self.confd, self.name)
    with open(filename, 'w') as f:
      f.write(upstreamString)
      f.close()
    self.reload()

  def removeUpstreamConfig(self):

    filename = '%s/upstream-%s.conf' % (self.confd, self.name)
    if os.path.isfile(filename):
      os.remove(filename)

  def reload(self):
    command = Cli.Command()
    command.execute("service nginx reload")



  # callable methods
  def status(self):
    pass

  def start(self):
    # should optimize and do that only on creation of the container
    self.writeUpstreamConfig()
    pass

  def stop(self):
    pass

  def restart(self):
    pass

  def destroy(self):
    self.removeUpstreamConfig()
    pass