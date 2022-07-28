class Job(object):
    """
    A class that creates jobs.

    Parameters
    ----------
    r: list - A list with the task sequence
    p: list - Processing times for every task
    """

    def __init__(self, id, r = None, p = None):
        self.id = id

        if r is None:
            self.r = [] # machine_routes
        else:
            self.r = r
        
        if p is None:
            self.p = [] # processing times
        else:
            self.p = p

        # TODO
        self.d = []  # due dates

    def get_duration_sum(self):
        return sum(self.p)

    def add_operation(self, r, p):
        self.r.append(r)
        self.p.append(p)

    def get_operation_count(self):
        return len(self.r)

    def __repr__(self) -> str:
        return "Id: {},\nMachine routes: {},\nProcessing times: {}\n".format(self.id, self.r, self.p)

    def get_tuple_list_representation(self):
        return [(r, p) for r, p in zip(self.r, self.p)]

    def get_operation_as_tuple(self, operation_index):
        return (self.r[operation_index], self.p[operation_index])

    def get_machine_route_list(self):
        return self.r

    def get_processing_time_list(self):
        return self.p