#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

origin=(3,8)

points=[(3,2),(4,5),(7,3),(8,3),(2,5),(4,2),(5,6),(5,8)]
points.append(origin)
distances={}

for elt in points:
    diff={}
    for point in points:
        if point != elt:
            if points.index(point)!=points.index(origin):
                diff[points.index(point)]=math.sqrt((elt[0]-point[0])**2+(elt[1]-point[1])**2)
        distances[points.index(elt)]=diff

ranged=[]
ranged_index=[]

def min_dist(dic):
    min=None
    min_key=None
    for key in dic.keys():
        if min is None:
            min=dic[key]
            min_key=key
        if dic[key]<min:
            min=dic[key]
            min_key=key
    return min_key


for i in distances.keys():
    if len(distances[i]) != 0:
        min=min_dist(distances[i])
        ranged.append(points[min])
        ranged_index.append(min)
        for k in distances.keys():
            if k!=min:
                distances[k].pop(min)
    

print(ranged)
print(ranged_index)
        