from src.base.job import Job
from src.base.jobshop import Jobshop
from src.shiftingbottleneck.shift import Shift
from src.io.jobshoploader import JobShopLoader

import matplotlib.pyplot as plt
import networkx as nx


#########################################################
#                       Instance 1
#########################################################

def plot_graph_with_machine_clique_colors(g):
    pass

def plot_graph_with_job_colors(g):
    pass

'''
instance_filename = "data/instances/taillard/ta01.txt"
jobs = JobShopLoader.load_jobshop(instance_filename)
'''

js = Shift()

jobs = {}
jobs[1] = Job(1, [1,2,3], [10, 8, 4])
jobs[2] = Job(2, [2,1,4,3], [8,3,5,6])
jobs[3] = Job(3, [1,2,4], [4,7,3])


js.addJobs(jobs)

#for node, data in js.nodes(data=True):
#    print(data)


js.criticalPath
js.output()

js.computeLmax()

js.add_edges_from([((1,1), (1,2)), ((1,2),(1,3))])

js.criticalPath
print(js.makespan)

color_map = ['red' if node == "V" or node == "U" else 'green' for node in js]


nx.draw(js,pos=nx.spring_layout(js),node_color=color_map,node_shape='o',edge_color='black',with_labels=True,font_size=10,node_size=500)
plt.show()
exit()


#########################################################
#                       Instance 2
#########################################################


js = Shift()
jobs = {}
jobs[1] = Job(1, [1,2], [3,4])
jobs[2] = Job(2, [1,2], [6,5])
jobs[3] = Job(3, [1,2], [4,5])
jobs[4] = Job(4, [1,2], [3,2])
jobs[11] = Job(11, [1,2], [12,2])

js.addJobs(jobs)
js.criticalPath
js.output()
print(sum(js.nodes[ij]['p'] for ij in js.machines[1]))
print(sum(js.nodes[ij]['p'] for ij in js.machines[2]))

seq = (3,2,1,11,4)
for j1, j2 in zip(seq[:-1], seq[1:]):
    js.add_edge((1,j1), (1,j2))

js.criticalPath
js.output()