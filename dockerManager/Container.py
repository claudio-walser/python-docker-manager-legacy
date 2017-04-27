import Cli
import os
import shutil
import json
import time

class Container(object):

  id = None
  name = None
  running = False
  created = False
  settings = {}
  dockerSettings = {}
  interface = None
  command = None

  def __init__(self, name, settings):
    self.name = name
    self.settings = settings
    self.interface = Cli.Interface()
    self.command = Cli.Command()
    self.getId()
    if self.id is not None:
      self.created = True
      self.inspect()

  def inspect(self):
    output = self.command.execute("docker inspect %s" % self.id)
    if output is False:
      return False
    self.dockerSettings = json.loads(output)[0]
    self.running = self.dockerSettings['State']['Running']

  def getName(self):
    return self.name

  def getIpAddress(self):
    if self.running:
      return self.dockerSettings['NetworkSettings']['IPAddress']

  def getId(self):
    if self.id:
      return self.id

    output = self.command.execute('docker ps -aqf "name=%s"' % self.name)
    if output == '':
      return None

    self.id = output
    return self.id

  def isRunning(self):
    return self.running

  def isCreated(self):
    return self.created

  def create(self):
    self.interface.header("Create %s" % self.name)
    if 'sourceVolumes' in self.settings:
      for sourceVolume in self.settings['sourceVolumes']:
        if not os.path.isdir(sourceVolume['target']):
          shutil.copytree(sourceVolume['source'], sourceVolume['target'])
    volumeString = ''
    if 'volumes' in self.settings:
      for volume in self.settings['volumes']:
        if not os.path.isdir(volume['source']):
          self.interface.error("Volume source %s does not exist! - skipping" % volume['source'])
          continue

        if 'uid' in volume:
          self.command.execute('chown -R %s %s' % (volume['uid'], volume['source']))
        volumeString += '-v=%s:%s ' % (volume['source'], volume['target'])

    dnsString = ''
    if 'dns' in self.settings:
      dnsString = '--dns=%s' % self.settings['dns']

    restartString = ''
    if 'restart' in self.settings:
      restartString = '--restart=%s' % self.settings['restart']

    exposeString = ''
    if 'expose' in self.settings:
      for expose in self.settings['expose']:
        exposeString += '--expose=%s ' % expose

    environmentString = ''
    if 'environment' in self.settings:
      for environment in self.settings['environment']:
        environmentString += '-e %s ' % environment

    privilegedString = ''
    if "privileged" in self.settings:
      privilegedString = '--privileged'

    cpuString = ''
    if 'cpus' in self.settings:
      cpuString += '--cpus="%s"' % (self.settings['cpus'])

    capAddString = ''
    if 'capAdd' in self.settings:
      capAddString += '--cap-add="%s"' % (self.settings['capAdd'])

    portMappingString = ''
    if 'portMapping' in self.settings:
      for portMapping in self.settings['portMapping']:
        portMappingString += '-p %s ' % portMapping

    command = 'docker run -d -it \
    --name=%s\
    --hostname=%s\
    %s\
    %s\
    %s\
    %s\
    %s\
    %s\
    %s\
    %s\
    %s\
    %s\
    ' % (self.name, self.name, portMappingString, cpuString, capAddString, environmentString, privilegedString, exposeString, volumeString, restartString, dnsString, self.settings['image'])
    print(command)
    self.id = self.command.execute(command)
    self.created = True
    self.waitForIp()

  def waitForIp(self):
    self.inspect()
    if self.getIpAddress() is None:
      return self.waitForIp()

    return True

  # callable methods
  def status(self):
    self.interface.header("Status of %s" % self.name)
    self.interface.writeOut("ContainerID: %s" % self.getId())
    self.interface.writeOut("Container IP Address: %s" % self.getIpAddress())
    self.interface.writeOut("Container is created: %s" % self.isCreated())
    self.interface.writeOut("Container running: %s" % self.isRunning())

  def start(self):
    if not self.created:
      self.create()
      return True

    self.interface.header("Start %s" % self.name)
    if not self.running:
      self.command.execute('docker start %s' % self.id)
      self.inspect()

  def stop(self):
    self.interface.header("Stop %s" % self.name)
    if self.running:
      self.command.execute('docker stop %s' % self.id)

  def restart(self):
    self.interface.header("Restart %s" % self.name)
    self.stop()
    self.start()


  def destroy(self):
    self.interface.header("Destroy %s" % self.name)
    if self.created:
      self.command.execute('docker rm -f %s' % self.id)
