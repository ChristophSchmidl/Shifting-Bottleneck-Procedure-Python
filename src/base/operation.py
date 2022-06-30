'''
This class is not really used atm but it is here for future reference.
'''
class Operation:
  def __init__(self, job_id, machine_id, duration):
    self.job_id = job_id # Integer
    self.machine_id = machine_id # Integer
    self.duration = duration # Integer

  def __repr__(self):
    return "Job ID: {},\nMachine ID: {},\nDuration: {}".format(
      str(self.job_id), 
      str(self.machine_id), 
      str(self.duration))