from itertools import permutations
from src.base.jobshop import Jobshop
from src.shiftingbottleneck.utils import argmin_kv


class Shift(Jobshop):
    def output(self):
        print("makespan: ", self.makespan)
        for i in self.machines:
            print("Machine: "+str(i))
            s = "{0:<7s}".format("jobs:")
            for ij in sorted(self.machines[i]):
                if ij in ("U", "V"):
                    continue
                s += "{0:>5d}".format(ij[1])
            print(s)
            s = "{0:<7s}".format("p:")
            for ij in sorted(self.machines[i]):
                if ij in ("U", "V"):
                    continue
                s += "{0:>5d}".format(self.nodes[ij]['p'])
            print(s)
            s = "{0:<7s}".format("r:")
            for ij in sorted(self.machines[i]):
                if ij in ("U", "V"):
                    continue
                s += "{0:>5d}".format(self.nodes[ij]['S'])
            print(s)
            s = "{0:<7s}".format("d:")
            for ij in sorted(self.machines[i]):
                if ij in ("U", "V"):
                    continue
                s += "{0:>5d}".format(self.nodes[ij]['Cp'])
            print(s)
            print("\n")
    
    def computeLmax(self):
        for m in self.machines:
            lateness = {}
            for seq in permutations(self.machines[m]):
                release = [self.nodes[j]['S'] for j in seq]
                due = [self.nodes[j]['Cp'] for j in seq]
                finish = [0]*len(release)
                for i, j in enumerate(seq):
                    finish[i] = max(finish[i-1], release[i]) +self.nodes[j]['p']
                late = max([f-d for d,f in zip(due,finish)])
                lateness[seq] = late
            s, l = argmin_kv(lateness)
            print("Machine: {}, lateness: {}, optimal seq: {}".format(m, l, s))