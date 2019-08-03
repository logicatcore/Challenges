#! /usr/bin/env python
import json
import numpy as np
from operator import itemgetter

with open('generatedGraph.json') as G:
    # N-odes + T-arget + S-ource + C-cost information in dict (dictionary) format
    ntsc = json.load(G)
# Assigning shorthand notation for accessing dict entries u --> unicode
N = u'nodes'
L = u'label'

E = u'edges'
T = u'target'
S = u'source'
C = u'cost'

# Index of Earth. Return value is int ##18##
earth =  ntsc[N].index({L: u'Erde'})
# Index of Destination planet. Return value is int ##246##
destination =  ntsc[N].index({L: u'b3-r7-r4nd7'})
# print earth, destination

# Ledger to keep track of all the planets connected to one planet
ledger = np.zeros((1000,50),dtype=np.int)

# Cost of reaching a particular planet is stored in individual locations
cost = []
for i in range(1000):
    cost.append(0.0)

# Path taken to reach a planet is kept track for every planet
path = []
for i in range(1000):
    path.append(0)

def main(flag):
    routefound = flag
    # Visited nodes/planets
    global vin
    vin = []
    # Branching/number of routes from every planet that we visit is tracked
    spawn = []
    cn = initialise()
    # current cost
    cc = 0
    # Add the current node to the list of visited nodes list
    vin.append(cn)
    # print 'Visited nodes:', vin
    # print cn
    # Path taken to arrive at Earth [18]
    path[cn] = [cn]
    # Neighbbouring planets to Earth and the respective costs
    unvin,costs = neigh(cn)
    # Progressively appends the branching number of the planets to this list
    spawn.append(len(unvin))
    q = 0
    while not routefound:
        # stepbystep = input('Enter any number to continue executing in steps: ')
        i = 0
        for n,c in zip(unvin,costs):
            # print 'current node: ',n
            if cn == 18:
                vin.append(n)
                # print 'Visited nodes:', vin
                cc = c
                pn = cn
                cn = n
                if cost[n] == 0 or cc < cost[n]:
                    cost[n] = cc
                    path[cn] = path[pn] + [cn]
                    # print 'Path: ',path[cn]
                # Remove the visited nodes/planets and the corresponding costs from the un-visited-nodes list
                unvin.remove(n)
                costs.remove(c)
                # Find and append the new planets to be visited and the costs to the un-visited-nodes list
                tempn,tempc = neigh(cn)
                spawn.append(len(tempn))
                unvin = unvin + tempn
                # print 'New unvisited nodes:', unvin
                costs = costs+ tempc

            else:
                # Using spawn to keep a correct track of the origin and hence to find the right path
                i = i+1
                if spawn[q+1] == 0:
                    q = q+1
                    if spawn[q+1] == 0:
                        q = q+1

                if i <= spawn[q+1]:
                    pn = vin[q+1]
                    # print 'Previous node as per new logic: ',pn
                    if i == spawn[q+1]:
                        i = 0
                        q = q+1


                vin.append(n)
                # print 'Visited nodes:', vin
                cn = n
                cc = cost[pn] + c
                # Dijkstra's relaxation
                if cost[n] == 0 or cc < cost[n]:
                    cost[n] = cc
                    path[cn] = path[pn] + [cn]
                    # print 'Path of ',cn,' is:',path[cn]
                # Remove the visited nodes/planets and the corresponding costs from the un-visited-nodes list
                unvin.remove(n)
                costs.remove(c)
                # Find and append the new planets to be visited and the costs to the un-visited-nodes list
                tempn,tempc = neigh(cn)
                spawn.append(len(tempn))
                # print 'spawn: ',spawn
                unvin = unvin + tempn
                # print 'New unvisited nodes:', unvin
                costs = costs+ tempc

                if cn == destination:
                    routefound = True
                    print path[cn]
                    print("{0:.17f}".format(cost[cn]))
                    break


def initialise():
    # Curreent node is set to Earth
    cn = earth
    return cn

def neigh(cn):
    cn = cn
    # Since the graph is undirected, we find all the possibile routes from a planet
    temp = [x for x in  ntsc[E] if (x[S] == cn or x[T] == cn)]
    # print temp
    # Sorting the routes based on the cost
    temp = sorted(temp, key=itemgetter(u'cost'))
    indices = []
    costs = []
    for x in temp:
        # Add the planets in ascending order to the un-visited-nodes/planets
        # list only if it's not already been visited
        if x[T] != cn and x[T] not in vin:
            indices.append(x[T])
            costs.append(x[C])
        elif x[S] not in vin:
            indices.append(x[S])
            costs.append(x[C])
    ledger[cn,0:len(indices)] = indices
    # print 'Indices and costs: ', indices,costs
    return indices,costs


if __name__=='__main__':
    routefound = False
    main(routefound)
