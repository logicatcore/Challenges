#! /usr/bin/env python
import json
import random as r
import math

with open('generatedGraph.json') as G:
    # N-odes + T-arget + S-ource + C-cost information in dict (dictionary) format
    ntsc = json.load(G)


for i in range(1000):
    # radius of the circle
    circle_r = 10
    # random angle
    alpha = 2 * math.pi * r.random()
    # random radius
    radius = circle_r * math.sqrt(r.random())
    # calculating coordinates
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)
    if i==18:
        ntsc[u'nodes'][i][u'id'] = str(i)
        ntsc[u'nodes'][i][u'label'] = 'EARTH'
        # ntsc[u'nodes'][i][u'x'] = r.uniform(0,1) *1000
        ntsc[u'nodes'][i][u'x'] = x
        ntsc[u'nodes'][i][u'y'] = y
        # ntsc[u'nodes'][i][u'y'] = r.uniform(0,1) *1000
        ntsc[u'nodes'][i][u'color'] = 'rgb(255,0,0)'
        ntsc[u'nodes'][i][u'size'] = 10
    elif i==246:
        ntsc[u'nodes'][i][u'id'] = str(i)
        ntsc[u'nodes'][i][u'label'] = str(ntsc[u'nodes'][i][u'label'])
        ntsc[u'nodes'][i][u'x'] = x
        ntsc[u'nodes'][i][u'y'] = y
        # ntsc[u'nodes'][i][u'x'] = r.uniform(0,1) *10000
        # ntsc[u'nodes'][i][u'y'] = r.uniform(0,1) *10000
        ntsc[u'nodes'][i][u'color'] = 'rgb(255,0,0)'
        ntsc[u'nodes'][i][u'size'] = 10
    else:
        ntsc[u'nodes'][i][u'id'] = str(i)
        ntsc[u'nodes'][i][u'label'] = str(ntsc[u'nodes'][i][u'label']).split('_')[1]
        ntsc[u'nodes'][i][u'x'] = x
        ntsc[u'nodes'][i][u'y'] = y
        # ntsc[u'nodes'][i][u'x'] = r.uniform(0,1) *10000
        # ntsc[u'nodes'][i][u'y'] = r.uniform(0,1) *10000
        ntsc[u'nodes'][i][u'color'] = '#FFC000'#'#FFD800'
        ntsc[u'nodes'][i][u'size'] = r.uniform(0,1)

for i in range(1500):
    ntsc[u'edges'][i]['id'] = str(i)

    del ntsc[u'edges'][i][u'cost']
    ntsc[u'edges'][i]['color'] = '#919098'
    ntsc[u'edges'][i][u'size'] = 10


    if ntsc[u'edges'][i][u'source'] == 18 and ntsc[u'edges'][i][u'target'] == 810:
        ntsc[u'edges'][i]['color'] = 'rgb(255,0,0)'
        ntsc[u'edges'][i][u'size'] = 1000
    if ntsc[u'edges'][i][u'source'] == 595 and ntsc[u'edges'][i][u'target'] == 810:
        ntsc[u'edges'][i]['color'] = 'rgb(255,0,0)'
        ntsc[u'edges'][i][u'size'] = 1000
    if ntsc[u'edges'][i][u'source'] == 132 and ntsc[u'edges'][i][u'target'] == 595:
        ntsc[u'edges'][i]['color'] = 'rgb(255,0,0)'
        ntsc[u'edges'][i][u'size'] = 1000
    if ntsc[u'edges'][i][u'source'] == 132 and ntsc[u'edges'][i][u'target'] == 519:
        ntsc[u'edges'][i]['color'] = 'rgb(255,0,0)'
        ntsc[u'edges'][i][u'size'] = 1000
    if ntsc[u'edges'][i][u'source'] == 71 and ntsc[u'edges'][i][u'target'] == 519:
        ntsc[u'edges'][i]['color'] = 'rgb(255,0,0)'
        ntsc[u'edges'][i][u'size'] = 1000
    if ntsc[u'edges'][i][u'source'] == 71 and ntsc[u'edges'][i][u'target'] == 432:
        ntsc[u'edges'][i]['color'] = 'rgb(255,0,0)'
        ntsc[u'edges'][i][u'size'] = 1000
    if ntsc[u'edges'][i][u'source'] == 246 and ntsc[u'edges'][i][u'target'] == 432:
        ntsc[u'edges'][i]['color'] = 'rgb(255,0,0)'
        ntsc[u'edges'][i][u'size'] = 1000

    ntsc[u'edges'][i][u'target'] = str(ntsc[u'edges'][i][u'target'])
    ntsc[u'edges'][i][u'source'] = str(ntsc[u'edges'][i][u'source'])


with open('modified.json', 'w') as outfile:
    json.dump(ntsc, outfile)
# json.dump(ntsc, 'modified.json')
