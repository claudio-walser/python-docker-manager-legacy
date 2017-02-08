import os
import Cli


class Nginx(object):

  settings = None
  containerName = None
  confd = '/etc/nginx/conf.d'

  def __init__(self, containerName, settings):
    self.containerName = containerName
    self.settings = settings

  def writeUpstreamConfig(self):
    upstreamString = 'upstream %s {\n' % self.containerName
    for i in range(0, self.settings['maxContainers']):
      upstreamString += '    server %s-%s' % (self.containerName, i)
      if 'backendPort' in self.settings['nginx']:
        upstreamString += ':%s' % (self.settings['nginx']['backendPort'])
      upstreamString += '\n'

    upstreamString += '}'

    filename = '%s/upstream-%s.conf' % (self.confd, self.containerName)
    with open(filename, 'w') as f:
      f.write(upstreamString)
      f.close()
    self.reload()

  def removeUpstreamConfig(self):
    filename = '%s/upstream-%s.conf' % (self.confd, self.containerName)
    os.remove(filename)

  def reload(self):
    command = Cli.Command()
    command.execute("service nginx reload")



  # callable methods
  def status(self):
    pass

  def start(self):
    # should optimize and do that only on creation of the container
    self.writeUpstreamConfig(self.container.getIpAddress(), self.container.getName())
    pass

  def stop(self):
    pass

  def restart(self):
    pass

  def destroy(self):
    self.removeUpstreamConfig()
    pass