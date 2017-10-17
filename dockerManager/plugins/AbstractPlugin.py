
class AbstractPlugin(object):

  # callable methods
  def status(self):
    pass

  def start(self):
    pass

  def stop(self):
    pass

  def restart(self):
    pass

  def destroy(self):
    pass

  def update(self):
    pass
