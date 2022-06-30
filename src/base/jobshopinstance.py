import os
from src.base.operation import Operation

class JobShopInstance:
  def __init__(self, filename, name, job_count, machine_count):
      self.filename = filename
      self.name = name
      self.job_count = job_count
      self.machine_count = machine_count
      self.jobs = []
    
  def add_job(self, job):
      self.jobs.append(job)

  def get_horizon(self):
      '''
      The horizon is the sum of all operation durations. 
      It gives you the worst makespan if every job is scheduled after each other.
      '''
      return sum(job.get_duration_sum() for job in self.jobs)

  def get_operation_count(self):
      return sum(job.get_operation_count() for job in self.jobs)

  def get_operation(self, job_id, operation_index):
      #return self.all_operations[job_id][operation_index]
      #return self.jobs[job_id][operation_index]
      first = next(filter(lambda job: job.job_id == job_id, self.jobs), None)
      return first[operation_index]

  def get_job(self, job_id):
      return self.jobs[job_id]    

  def print_report(self):
      print("\nJob-shop problem instance in JSSP format read from file: {}".format(self.filename))
      print("Name: {}".format(self.name))
      print("Number of jobs: {}".format(self.job_count))
      print("Number of machines: {}".format(self.machine_count))
      print("Number of operations: {}".format(self.get_operation_count()))
      print("Horizon (duration sum): {}".format(self.get_horizon()))
      print("==========================================\n")

      '''
      for idx, job in enumerate(self.all_operations):
          print("Job: {}\n".format(idx))

          for operation in job:
              print((operation.machine_id, operation.duration))
          print("\n")
      '''

  def get_jobs_as_list_of_tuples_with_job_id(self):
      return [(job.Id, job.get_tuple_list_representation()) for job in self.jobs]

  def get_jobs_as_list_of_tuples(self):
      return [job.get_tuple_list_representation() for job in self.jobs]

  def print_raw_contents(self):
      pass