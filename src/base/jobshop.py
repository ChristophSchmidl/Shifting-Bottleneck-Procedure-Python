import networkx as nx


class Jobshop(nx.DiGraph):
    """
    A class that creates a directed graph of a jobshop.

    We formulate the tasks of the jobshop as nodes in a directed graph, add the processing 
    times of the tasks as attributes to the task nodes. A flag "dirty" was added so when 
    some topological changes are carried the method "_update" is called first to update 
    the makespan and critical path values. Once the update is finished, the updated 
    makespan is returned.

    Methods
    -------
    handleJobRoutings(jobs)
        Creates the edges of the graph that represents the given route and also adds 
        the origin and finishing nodes.

    handleJobProcessingTimes(jobs)
        Creates the nodes of the graph that represent the tasks of a job.

    makeMachineSubgraphs()
        For every given machine creates a subgraph.

    addJobs(jobs)
        Handles the routine to add a jobs to the graph and the subgraphs.

    output()
        Prints the output. 
    
    _forward

    _backward

    _computeCriticalPath

    _update

    Properties
    ----------
    makespan

    criticalPath

    """

    def __init__(self):
        super().__init__()
        #a dictionary to store machine's id of a subgraph with its jobs and routing
        self.machines = {}
        #start node
        self.add_node("U", p=0)
        #finish node
        self.add_node("V", p=0)
        #set dirty flag
        self._dirty = True
        #set initial makespan
        self._makespan = -1
        #define criticla path
        self._criticalPath = None

    def add_node(self, *args, **kwargs):
        #adds dirty flag so the the _update subroutine is called 
        self._dirty = True
        super().add_node(*args, **kwargs)

    def add_nodes_from(self, *args, **kwargs):
        #adds dirty flag so the the _update subroutine is called 
        self._dirty = True
        super().add_nodes_from(*args, **kwargs)

    def add_edge(self, *args):
        #adds dirty flag so the the _update subroutine is called 
        self._dirty = True
        super().add_edge(*args)

    def add_edges_from(self, *args, **kwargs):
        #adds dirty flag so the the _update subroutine is called 
        self._dirty = True
        super().add_edges_from(*args, **kwargs)

    def remove_node(self, *args, **kwargs):
        #adds dirty flag so the the _update subroutine is called 
        self._dirty = True
        super().remove_node(*args, **kwargs)

    def remove_nodes_from(self, *args, **kwargs):
        #adds dirty flag so the the _update subroutine is called 
        self._dirty = True
        super().remove_nodes_from(*args, **kwargs)

    def remove_edge(self, *args):
        #adds dirty flag so the the _update subroutine is called 
        self._dirty = True
        super().remove_edge(*args)

    def remove_edges_from(self, *args, **kwargs):
        #adds dirty flag so the the _update subroutine is called 
        self._dirty = True
        super().remove_edges_from(*args, **kwargs)

    def handleJobRoutings(self, jobs):
        for j in jobs.values():
            #add start edge
            self.add_edge("U", (j.r[0], j.Id))
            #add the edges (processing order) routing the nodes (tasks)
            for m, n in zip(j.r[:-1], j.r[1:]):
                self.add_edge((m, j.Id), (n, j.Id))
            #add finishing edge
            self.add_edge((j.r[-1], j.Id), "V")

    def handleJobProcessingTimes(self, jobs):
        for j in jobs.values():
            #add every task and its corresponding processing time to the graph
            for m, p in zip(j.r, j.p):
                self.add_node((m, j.Id), p=p)

    def makeMachineSubgraphs(self):
        #creates a set with machines' ids
        machineIds = set(ij[0] for ij in self if ij[0] not in ("U", "V"))
        #for every machine in the digraph creates a subgraph linked to the id with the corresponfing nodes
        for m in machineIds:
            self.machines[m] = self.subgraph(ij for ij in self if ij[0] == m not in ("U", "V"))
            #self.machines[m].remove_nodes_from(["U", "V"])

    def addJobs(self, jobs):
        #every time a job is inserted: add the jobs' edges (routing), jobs' nodes (tasks), 
        # and creates a subgraph for every machine
        self.handleJobRoutings(jobs)
        self.handleJobProcessingTimes(jobs)
        self.makeMachineSubgraphs()

    def output(self):
        #neatly outputs the jobshop digraph
        for m in sorted(self.machines):
            for j in sorted(self.machines[m]):
                print("{}: {}".format(j, self.nodes[j]['C']))

    def _forward(self):
        for n in nx.topological_sort(self):
            S = max([self.nodes[j]['C'] for j in self.predecessors(n)], default = 0)
            self.add_node(n, S = S, C = S + self.nodes[n]['p'])

    def _backward(self):
        for n in list(reversed(list(nx.topological_sort(self)))):
            Cp = min([self.nodes[j]['Sp'] for j in self.successors(n)], default = self._makespan)
            self.add_node(n, Sp = Cp - self.nodes[n]['p'], Cp = Cp)

    def _computeCriticalPath(self):
        G = set()
        for n in self:
            if self.nodes[n]['C'] == self.nodes[n]['Cp']:
                G.add(n)
        self._criticalPath = self.subgraph(G)

    @property
    def makespan(self):
        if self._dirty:
            self._update()
        return self._makespan

    @property
    def criticalPath(self):
        if self._dirty:
            self._update()
        return self._criticalPath

    def _update(self):
        self._forward()
        self._makespan = max(nx.get_node_attributes(self, 'C').values())
        self._backward()
        self._computeCriticalPath()
        self._dirty = False