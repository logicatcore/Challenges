# Program working

# Task
Find the only route from planet Erde to b3-r7-r4nd7 i.e, node 18 to node 246 among 1000 planets and 1500 routes possible in a undirected graph/map which allows moving from one planet to another.

# Interpreter and language used
Python

# Working of code

 -> Works based on Dijkstra's algorithm of single source and single destination

 -> Planets are visited based on least cost basis. The sub planets are recursively visited after one complete sweep again in least cost basis.

 -> Relaxation, current cost, current node, actual path of every planet is kept track

 -> Execution stops when we reach our destination i.e, planet 246
