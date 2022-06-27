import os
from classes import Job

class JobShopLoader:
    @staticmethod
    def load_jobshop(filename, format="JSSP"):
        '''
        Follows the JSSP format
        '''
        if format == "JSSP":
            return JobShopLoader._load_jssp_jobshop(filename)
        else:
            raise NotImplementedError()

    @staticmethod
    def _load_jssp_jobshop(filename):
        with open(filename) as f:
            lines = f.readlines()
        
        first_line = lines[0].split()
      
        # Name of instance
        name = os.path.split(filename)[-1]
        # Number of jobs
        job_count = int(first_line[0])
        # Number of machines
        machine_count = int(first_line[1])

        # Create a nested list of all operations
        #all_operations = [ [] for _ in range(job_count) ]

        jobs = {}

        for job_id, line in enumerate(lines[1:]):
            machine_duration_array = line.split()

            new_job = Job(Id=job_id, r=[], p=[])

            it = iter(machine_duration_array)  
            for machine_id, duration in list(zip(it, it)):
                new_job.r.append(int(machine_id))
                new_job.p.append(int(duration))
            
            jobs[job_id] = new_job

        return jobs
